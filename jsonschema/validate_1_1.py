#!/usr/bin/env python3
"""Convert a valid DCAT-US v1.1 catalog to a valid DCAT-US v3.0 catalog."""
import json
import re
from pathlib import Path

import click
from curl_cffi import requests
from curl_cffi.requests.exceptions import RequestException
from jsonschema import Draft202012Validator
from referencing import Registry, Resource


V1_1_CATALOG_SCHEMA_ID = "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
SCRIPT_DIR = Path(__file__).parent
V1_1_DEFINITIONS_DIR = SCRIPT_DIR / "v1.1_definitions"
PATTERN_DESCRIPTIONS = {
    "mailto": "invalid mailto URI format",
    "R\\/P": "invalid ISO 8601 duration",
    r"[\+-]?\d{4}.*\/": "invalid ISO 8601 interval",
    r"R\d*\/": "invalid ISO 8601 repeating interval",
    "[0-9]{3}:[0-9]{3}": "invalid program code format (expected '###:###')",
    "[0-9]{3}-[0-9]{9}": "invalid IT investment UII format (expected '###-#########')",
    r"[\+-]?\d{4}(?!\d{2}": "invalid ISO 8601 date/datetime",
}


class CatalogFetchException(Exception):
    pass


class CatalogValidationException(Exception):
    pass


def _describe_pattern(pattern: str) -> str:
    """Return a human-readable description for a known regex pattern, or None."""
    for substring, description in PATTERN_DESCRIPTIONS.items():
        if substring in pattern:
            return description
    return None


def format_path(path):
    """Format a jsonschema path as a readable string like 'subject[0].inScheme'."""
    if not path:
        return "(root)"
    parts = []
    for p in path:
        if isinstance(p, int):
            # Array index - append to previous part
            if parts:
                parts[-1] = f"{parts[-1]}[{p}]"
            else:
                parts.append(f"[{p}]")
        else:
            parts.append(str(p))
    return ".".join(parts)


def format_validation_errors(errors, indent=0):
    """Summarize validation errors grouped by type with occurrence counts."""
    prefix = "  " * indent
    counts = {}

    for error in errors:
        summary = summarize_error(error)
        if not summary:
            continue
        # Normalize array indices to [N] so errors from different items group together
        key = re.sub(r'\[\d+\]', '[N]', summary)
        counts[key] = counts.get(key, 0) + 1

    if not counts:
        return ""

    # Sort by count descending, then alphabetically for stable output
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    lines = []
    for msg, count in sorted_items:
        noun = "dataset" if count == 1 else "datasets"
        lines.append(f"{prefix}{msg}: {count} {noun}")

    return "\n".join(lines)


def summarize_error(error, prefix="", is_suberror=False):
    """Summarize a single error into a human-readable string."""
    path = format_path(error.path)

    # Handle anyOf/oneOf errors by finding meaningful sub-errors
    if error.validator in ("anyOf", "oneOf") and error.context:
        meaningful = find_meaningful_errors(error.context)

        if not meaningful:
            return f"{prefix}{path}: field is not null and does not match any allowed type"

        has_null_alternative = any(is_null_type_error(e) for e in error.context)

        summaries = []
        for sub_error in meaningful:
            sub_summary = summarize_error(sub_error, prefix="", is_suberror=True)
            if sub_summary:
                summaries.append(sub_summary)

        # Collapse repeated identical sub-errors to a single bullet
        unique_summaries = list(dict.fromkeys(summaries))

        if has_null_alternative and unique_summaries:
            intro = f"{path}: field is not null and "
            if len(unique_summaries) == 1:
                return f"{prefix}{intro}{unique_summaries[0]}"
            else:
                return f"{prefix}{intro}does not match alternatives:\n" + "\n".join(
                    f"{prefix}  - {s}" for s in unique_summaries
                )
        elif unique_summaries:
            if len(unique_summaries) == 1:
                return f"{prefix}{path}: {unique_summaries[0]}"
            else:
                return f"{prefix}{path}: does not match any alternative:\n" + "\n".join(
                    f"{prefix}    - {s}" for s in unique_summaries
                )

    # Handle $ref errors - find the expected class
    if "$ref" in error.schema:
        class_name = extract_schema_name(error.schema)
        if error.context:
            meaningful = find_meaningful_errors(error.context)
            if meaningful:
                sub_summaries = [summarize_error(e, prefix="", is_suberror=True) for e in meaningful]
                sub_summaries = [s for s in sub_summaries if s]
                if sub_summaries:
                    if class_name:
                        return f"does not conform to {class_name}: {'; '.join(sub_summaries)}"
                    return "; ".join(sub_summaries)
        if class_name:
            return f"does not conform to {class_name}"

    # Handle required field errors
    if error.validator == "required":
        missing = error.validator_value
        if isinstance(missing, list):
            missing_fields = [f for f in missing if f in error.message]
            if missing_fields:
                return f"missing required field '{missing_fields[0]}'"
        if "is a required property" in error.message:
            field = error.message.split("'")[1]
            return f"missing required field '{field}'"
        return error.message

    # Handle type errors
    if error.validator == "type":
        expected = error.validator_value
        if isinstance(expected, list):
            expected = " or ".join(expected)
        if is_suberror:
            return f"expected type '{expected}'"
        return f"{prefix}{path}: expected type '{expected}'"

    # Handle enum errors
    if error.validator == "enum":
        if is_suberror:
            return f"value not in allowed values: {error.validator_value}"
        return f"{prefix}{path}: value not in allowed values: {error.validator_value}"

    # Handle pattern errors
    if error.validator == "pattern":
        description = _describe_pattern(error.validator_value)
        msg = description if description else f"does not match pattern '{error.validator_value}'"
        if is_suberror:
            return msg
        return f"{prefix}{path}: {msg}"

    # Handle format errors
    if error.validator == "format":
        msg = f"invalid format, expected '{error.validator_value}'"
        if is_suberror:
            return msg
        return f"{prefix}{path}: {msg}"

    # Handle maxLength errors - omit the value to allow grouping
    if error.validator == "maxLength":
        msg = f"value is too long (max {error.validator_value} characters)"
        if is_suberror:
            return msg
        return f"{prefix}{path}: {msg}"

    # Default: use the message, prepending path if available
    if not is_suberror and path and path != "(root)":
        return f"{prefix}{path}: {error.message}"
    return f"{prefix}{error.message}"


def find_meaningful_errors(errors):
    """Filter errors to find the meaningful ones, skipping null-type failures."""
    meaningful = []
    for error in errors:
        if is_null_type_error(error):
            continue
        meaningful.append(error)
    return meaningful if meaningful else list(errors)


def is_null_type_error(error):
    """Check if this error is just 'type is not null'."""
    return (error.validator == "type" and
            error.validator_value == "null")


def extract_schema_name(schema):
    """Extract a human-readable schema/class name from a schema definition."""
    if isinstance(schema, dict):
        if "$ref" in schema:
            # Extract class name from ref like "/dcat-us/3.0.0/definitions/concept"
            ref = schema["$ref"]
            return ref.split("/")[-1].title()
        if "title" in schema:
            return schema["title"]
    return None


def load_schema_registry(definitions_dir: Path) -> Registry:
    registry = Registry()
    for schema_file in definitions_dir.glob("*.json"):
        with schema_file.open() as f:
            resource = Resource.from_contents(json.load(f))
            registry = resource @ registry
    return registry


def fetch_dcat_catalog(url: str) -> dict:
    """Fetch a DCAT-US v1.1 catalog to validate."""
    # Some target servers (e.g. usda.gov) reject non-browser TLS/HTTP2 fingerprints, so
		# we impersonate a real browser using curl_cffi.
    try:
        response = requests.get(url, timeout=60, impersonate="safari17_0")
        response.raise_for_status()
    except RequestException as e:
        raise CatalogFetchException(f"Request failed: {type(e).__name__}: {e!r}") from e

    try:
        text = response.content.decode("utf-8-sig")
        text = text.lstrip("\ufeff")
    except UnicodeDecodeError:
        text = response.content.decode("cp1252")

    try:
        data = json.loads(text)
        if isinstance(data, list):
            raise CatalogFetchException("Response is a JSON array, not a catalog object")
        return data
    except ValueError as e:
        raise CatalogFetchException(f"Response was not valid JSON: {e}") from e


def validate_catalog(schema_id: str, registry: Registry, catalog: dict) -> None:
    """Validate a catalog and raise CatalogValidationException if invalid."""
    validator = Draft202012Validator(
        {"$ref": schema_id},
        registry=registry,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
    errors = list(validator.iter_errors(catalog))
    if errors:
        version_number = "v1.1" if "v1.1" in schema_id else "v3.0"
        dataset_count = len(catalog.get("dataset", []))
        raise CatalogValidationException(
            f"{version_number} validation failed with {len(errors)} error(s) across {dataset_count} datasets:\n"
            + format_validation_errors(errors, indent=2)
        )


def filter_invalid_datasets(schema_id: str, registry: Registry, catalog: dict) -> tuple[dict, int]:
    """
    Return a copy of the catalog with invalid datasets removed, plus the count removed.

    Works by validating each dataset individually against the catalog schema.
    Datasets whose index appears in any top-level error path are dropped.
    """
    validator = Draft202012Validator(
        {"$ref": schema_id},
        registry=registry,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
    errors = list(validator.iter_errors(catalog))

    # Collect the indices of datasets implicated in at least one error.
    # jsonschema paths look like: deque(['dataset', 3, 'title', ...])
    bad_indices = set()
    for error in errors:
        path = list(error.absolute_path)
        if len(path) >= 2 and path[0] == "dataset" and isinstance(path[1], int):
            bad_indices.add(path[1])

    datasets = catalog.get("dataset", [])
    filtered = [ds for i, ds in enumerate(datasets) if i not in bad_indices]
    removed = len(datasets) - len(filtered)

    return {**catalog, "dataset": filtered}, removed


@click.command()
@click.option("-u", "--url", help="URL of DCAT-US v1.1 catalog to be converted", required=True)
def main(url):
    v1_1_registry = load_schema_registry(V1_1_DEFINITIONS_DIR)
    try:
        catalog_to_convert = fetch_dcat_catalog(url)
    except CatalogFetchException as e:
        click.echo(f"There was an error fetching a DCAT-US v1.1 catalog to convert: {e}", err=True)
        return 1

    try:
        validate_catalog(V1_1_CATALOG_SCHEMA_ID, v1_1_registry, catalog_to_convert)
    except CatalogValidationException as e:
        click.echo(f"Warning: catalog has invalid data, filtering it out:\n{e}", err=True)
        catalog_to_convert, removed = filter_invalid_datasets(
            V1_1_CATALOG_SCHEMA_ID, v1_1_registry, catalog_to_convert
        )
        remaining = len(catalog_to_convert.get("dataset", []))
        click.echo(f"Removed {removed} invalid dataset(s). {remaining} valid dataset(s) remaining.", err=True)
        if remaining == 0:
            click.echo("No valid datasets remain after filtering.", err=True)
            return 1

if __name__ == "__main__":
    main(standalone_mode=False)
