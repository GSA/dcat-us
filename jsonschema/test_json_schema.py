# import json
# import sys
# from pathlib import Path
# from jsonschema import Draft202012Validator





# def remove_nested_ids(obj, is_root=True):
#     """Remove $id from nested properties and rewrite $ref paths for Draft 2020-12."""
#     if isinstance(obj, dict):
#         result = {}
#         for key, value in obj.items():
#             if key == "$id" and not is_root:
#                 continue
#             if key == "$ref" and isinstance(value, str) and value.startswith("#/definitions/"):
#                 result[key] = value.replace("#/definitions/", "#/$defs/")
#             else:
#                 result[key] = remove_nested_ids(value, is_root=False)
#         return result
#     elif isinstance(obj, list):
#         return [remove_nested_ids(item, is_root=False) for item in obj]
#     return obj

# def load_schema_with_definitions(script_dir):
#     definitions_dir = script_dir / "definitions"
#     definitions = {}
    
#     for schema_file in definitions_dir.glob("*.json"):
#         with open(schema_file) as f:
#             schema = json.load(f)
#         schema = remove_nested_ids(schema)
#         schema_name = schema_file.stem
#         definitions[schema_name] = schema
    
#     return definitions

# def main():
#     script_dir = Path(__file__).parent
#     examples_dir = script_dir / "examples"
    
#     definitions = load_schema_with_definitions(script_dir)
    
#     failures = []
    
#     for example_file in examples_dir.rglob("*.json"):
#         rel_path = example_file.relative_to(examples_dir)
#         parts = rel_path.parts
        
#         if len(parts) < 3:
#             continue
        
#         schema_name = parts[0]
#         expected_result = parts[1]  # "good" or "bad"
        
#         if expected_result not in ("good", "bad"):
#             continue
        
#         if schema_name not in definitions:
#             print(f"SKIP: No schema found for {rel_path}")
#             continue
        
#         # Create a schema that references the specific definition
#         test_schema = {
#             "$schema": "https://json-schema.org/draft/2020-12/schema",
#             "$defs": definitions,
#             "$ref": f"#/$defs/{schema_name}"
#         }

#         with open(example_file) as f:
#             example = json.load(f)

#         validator = Draft202012Validator(test_schema)
#         errors = list(validator.iter_errors(example))
#         validation_passed = len(errors) == 0
        
#         if expected_result == "good" and validation_passed:
#             print(f"PASS: {rel_path}")
#         elif expected_result == "bad" and not validation_passed:
#             print(f"PASS: {rel_path}")
#         else:
#             outcome = "passed" if validation_passed else "failed"
#             print(f"FAIL: {rel_path} (expected {expected_result}, but validation {outcome})")
            

            
#             failures.append(str(rel_path))
    
#     if failures:
#         print(f"\n{len(failures)} test(s) failed")
#         sys.exit(1)
#     else:
#         print("\nAll tests passed")

# if __name__ == "__main__":
#     main()



import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource

def format_validation_errors(errors, indent=0):
    """Format validation errors with detailed field paths and nested sub-errors."""
    output = []
    prefix = "  " * indent
    
    for error in sorted(errors, key=lambda e: list(e.path)):
        field_path = ".".join(str(p) for p in error.path) if error.path else "(root)"
        schema_path = "/".join(str(p) for p in error.schema_path)
        
        output.append(f"{prefix}Field: {field_path}")
        output.append(f"{prefix}  Error: {error.message}")
        output.append(f"{prefix}  Schema path: {schema_path}")
        output.append(f"{prefix}  Validator: {error.validator}")
        
        if error.context:
            output.append(f"{prefix}  Sub-errors ({len(error.context)} alternatives failed):")
            output.append(format_validation_errors(error.context, indent + 2))
        
        output.append("")
    
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
