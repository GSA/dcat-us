import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource


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


def is_null_type_error(error):
    """Check if this error is just 'type is not null'."""
    return (error.validator == "type" and 
            error.validator_value == "null")


def find_meaningful_errors(errors):
    """Filter errors to find the meaningful ones, skipping null-type failures."""
    meaningful = []
    for error in errors:
        if is_null_type_error(error):
            continue
        meaningful.append(error)
    return meaningful if meaningful else list(errors)


def summarize_error(error, prefix=""):
    """Summarize a single error into a human-readable string."""
    path = format_path(error.path)
    
    # Handle anyOf/oneOf errors by finding meaningful sub-errors
    if error.validator in ("anyOf", "oneOf") and error.context:
        meaningful = find_meaningful_errors(error.context)
        
        # If all sub-errors are null-type, we have a different problem
        if not meaningful:
            return f"{prefix}{path}: field is not null and does not match any allowed type"
        
        # Check if it's a simple "not null and wrong type" case
        has_null_alternative = any(is_null_type_error(e) for e in error.context)
        
        summaries = []
        for sub_error in meaningful:
            sub_summary = summarize_error(sub_error, prefix="")
            if sub_summary:
                summaries.append(sub_summary)
        
        if has_null_alternative and summaries:
            intro = f"{path}: field is not null and "
            if len(summaries) == 1:
                return f"{prefix}{intro}{summaries[0]}"
            else:
                return f"{prefix}{intro}does not match alternatives:\n" + "\n".join(
                    f"{prefix}  - {s}" for s in summaries
                )
        elif summaries:
            if len(summaries) == 1:
                return f"{prefix}{path}: {summaries[0]}"
            else:
                return f"{prefix}{path}: does not match any alternative:\n" + "\n".join(
                    f"{prefix}    - {s}" for s in summaries
                )
    
    # Handle $ref errors - find the expected class
    if "$ref" in error.schema:
        class_name = extract_schema_name(error.schema)
        if error.context:
            # Dig into what specifically failed
            meaningful = find_meaningful_errors(error.context)
            if meaningful:
                sub_summaries = [summarize_error(e, prefix="") for e in meaningful]
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
        # Parse from message: "'fieldname' is a required property"
        if "is a required property" in error.message:
            field = error.message.split("'")[1]
            return f"missing required field '{field}'"
        return error.message
    
    # Handle type errors
    if error.validator == "type":
        expected = error.validator_value
        if isinstance(expected, list):
            expected = " or ".join(expected)
        return f"expected type '{expected}'"
    
    # Handle enum errors
    if error.validator == "enum":
        return f"value not in allowed values: {error.validator_value}"
    
    # Handle pattern errors
    if error.validator == "pattern":
        return f"does not match pattern '{error.validator_value}'"
    
    # Handle format errors
    if error.validator == "format":
        return f"invalid format, expected '{error.validator_value}'"
    
    # Default: use the message
    return error.message


def format_validation_errors(errors, indent=0):
    """Format validation errors with summarization and clear nesting."""
    output = []
    prefix = "  " * indent
    
    # Group errors by their root path for cleaner output
    for error in sorted(errors, key=lambda e: list(e.path)):
        summary = summarize_error(error, prefix=prefix)
        if summary:
            output.append(summary)
    
    return "\n".join(output)

def load_schema_registry(script_dir):
    registry = Registry()

    # the top-level schema is in script_dir/Catalog.json
    with open(script_dir / "Catalog.json") as f:
        schema_dict = json.load(f)
        resource = Resource.from_contents(schema_dict)
        registry = resource @ registry

    # lower-level schemas are in all the files in script_dir/definitions
    definitions_dir = script_dir / "definitions"

    for schema_file in definitions_dir.glob("*.json"):
        with open(schema_file) as f:
            schema_dict = json.load(f)
            resource = Resource.from_contents(schema_dict)
            registry = resource @ registry

    return registry

def main():
    script_dir = Path(__file__).parent
    examples_dir = script_dir / "examples"

    registry = load_schema_registry(script_dir)

    failures = []

    # check every JSON in the examples directory
    for example_file in examples_dir.rglob("*.json"):
        rel_path = example_file.relative_to(examples_dir)
        parts = rel_path.parts

        if len(parts) < 3:
            continue

        schema_name = parts[0]
        expected_result = parts[1]  # "good" or "bad"

        if expected_result not in ("good", "bad"):
            continue

        # TODO: Catalog has an id with a different structure
        schema_id = f"https://resources.data.gov/dcat-us/3.0.0/definitions/{schema_name.lower()}"
        try:
            schema_resource = registry[schema_id]
        except NoSuchResource:
            print(f"SKIP: No schema found for {schema_id} from {rel_path}")
            continue
        validator = Draft202012Validator({"$ref": schema_id}, registry=registry, format_checker=Draft202012Validator.FORMAT_CHECKER)

        with open(example_file) as f:
            example = json.load(f)

        errors = list(validator.iter_errors(example))
        validation_passed = len(errors) == 0

        if expected_result == "good" and validation_passed:
            print(f"PASS: {rel_path}")
        elif expected_result == "bad" and not validation_passed:
            print(f"PASS: {rel_path}")
        else:
            outcome = "passed" if validation_passed else "failed"
            print(f"FAIL: {rel_path} (expected {expected_result}, but validation {outcome})")
            failures.append(str(rel_path))
            
						# For good examples that failed, show detailed error information
            if expected_result == "good" and not validation_passed:
                print(f"\n  Validation errors for {rel_path}:")
                print(format_validation_errors(errors, indent=2))

    if failures:
        print(f"\n{len(failures)} test(s) failed")
        sys.exit(1)
    else:
        print("\nAll tests passed")

if __name__ == "__main__":
    main()
