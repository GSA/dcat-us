import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource

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
        validator = Draft202012Validator({"$ref": schema_id}, registry=registry)

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

    if failures:
        print(f"\n{len(failures)} test(s) failed")
        sys.exit(1)
    else:
        print("\nAll tests passed")

if __name__ == "__main__":
    main()
