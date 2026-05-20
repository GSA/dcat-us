#!/usr/bin/env python3
"""Convert a valid DCAT-US v1.1 catalog to a valid DCAT-US v3.0 catalog."""
import json
import sys
from pathlib import Path

import click
import requests
from jsonschema import Draft202012Validator
from referencing import Registry, Resource


V11_SCHEMA_URL = "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
V3_CATALOG_SCHEMA_ID = "https://resources.data.gov/dcat-us/3.0.0/definitions/catalog"
SCRIPT_DIR = Path(__file__).parent
V3_DEFINITIONS_DIR = SCRIPT_DIR / "definitions"

class CatalogFetchException(Exception):
    pass


class CatalogConversionException(Exception):
    pass


class CatalogValidationException(Exception):
    pass


# Example URL:
# - https://open.gsa.gov/data.json
def fetch_dcat_catalog(url: str) -> dict:
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as e:
        raise CatalogFetchException(str(e)) from e


def convert_dcat_catalog(old_catalog: dict) -> dict:
    raise NotImplementedError("convert_dcat_catalog is not yet implemented")

    # if any issues, raise CatalogConversionException

    # Breaking Change 1: fix modified

    # Breaking Change 2: fix temporal

    # Breaking Change 3: fix spatial

    # Breaking Change 4: fix language

    # Structural Change 1: Update conformsTo on the Catalog

    # Structural Change 2: Remove @context and describedBy from the Catalog

    # Structural Change 3: Replace accessLevel with accessRights

    # Structural Change 4: Add license to Distribution objects

    pass


def validate_v1_1(catalog: dict) -> None:
    # raise CatalogValidationException if invalid
    pass


def validate_v3_0(catalog: dict, registry: Registry) -> None:
    validator = Draft202012Validator(
        {"$ref": V3_CATALOG_SCHEMA_ID},
        registry=registry,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
    errors = list(validator.iter_errors(catalog))
    if errors:
        raise CatalogValidationException(
            f"v3.0 validation failed with {len(errors)} error(s): "
            + "; ".join(e.message for e in errors[:5])
        )


def export_converted_catalog(catalog, output_dir: str):
    pass


def load_v3_schema_registry(definitions_dir: Path) -> Registry:
    registry = Registry()
    for schema_file in definitions_dir.glob("*.json"):
        with schema_file.open() as f:
            resource = Resource.from_contents(json.load(f))
            registry = resource @ registry
    return registry


@click.command()
@click.option("-o", "--output-dir", help="Output directory", default="converted_dcat_data")
@click.option("-u", "--url", help="URL of DCAT-US v1.1 catalog to be converted", required=True)
def main(output_dir, url):
    """Convert DCAT catalog."""
    registry = load_v3_schema_registry(V3_DEFINITIONS_DIR)
    try:
        catalog_to_convert = fetch_dcat_catalog(url)
        validate_v1_1(catalog_to_convert)
        converted_catalog = convert_dcat_catalog(catalog_to_convert)
        validate_v3_0(converted_catalog, registry)
        export_converted_catalog(converted_catalog, output_dir)
    except CatalogFetchException as e:
        click.echo(f"There was an error fetching a DCAT-US v1.1 catalog to convert: {e}", err=True)
        sys.exit(1)
    except CatalogValidationException as e:
        click.echo(f"Invalid DCAT-US data: {e}", err=True)
        sys.exit(1)
    except CatalogConversionException as e:
        click.echo(f"There was an error converting a DCAT-US v1.1 catalog to DCAT-US v3.0: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
