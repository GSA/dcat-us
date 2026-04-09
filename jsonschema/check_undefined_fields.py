#!/usr/bin/env python3
"""
Check for fields in example files that are not defined in the JSON schema.

This script validates that example JSON files only use fields that are 
explicitly defined in their corresponding schema definitions. While the 
schemas may allow additional properties, examples should only demonstrate
documented fields.
"""

import json
import sys
from pathlib import Path


def load_schemas(script_dir):
    """Load all schema definitions into a dictionary keyed by schema name."""
    schemas = {}
    
    # Load top-level Catalog schema
    catalog_path = script_dir / "Catalog.json"
    if catalog_path.exists():
        with open(catalog_path) as f:
            schemas["catalog"] = json.load(f)
    
    # Load all definition schemas
    definitions_dir = script_dir / "definitions"
    for schema_file in definitions_dir.glob("*.json"):
        schema_name = schema_file.stem.lower()
        with open(schema_file) as f:
            schemas[schema_name] = json.load(f)
    
    return schemas


def resolve_ref(ref, schemas):
    """Resolve a $ref to get the actual schema definition."""
    # Format: "/dcat-us/3.0.0/definitions/concept" -> "concept"
    if ref.startswith("/dcat-us/"):
        schema_name = ref.split("/")[-1].lower()
        return schemas.get(schema_name)
    return None


def get_allowed_properties(schema, schemas):
    """
    Extract the set of allowed property names from a schema definition.
    Handles anyOf, oneOf, allOf, $ref, and direct properties.
    """
    allowed = set()
    
    if not isinstance(schema, dict):
        return allowed
    
    # Direct properties
    if "properties" in schema:
        allowed.update(schema["properties"].keys())
    
    # Handle $ref
    if "$ref" in schema:
        ref_schema = resolve_ref(schema["$ref"], schemas)
        if ref_schema:
            allowed.update(get_allowed_properties(ref_schema, schemas))
    
    # Handle anyOf/oneOf/allOf
    for keyword in ("anyOf", "oneOf", "allOf"):
        if keyword in schema:
            for sub_schema in schema[keyword]:
                allowed.update(get_allowed_properties(sub_schema, schemas))
    
    return allowed


def get_property_schema(prop_name, schema, schemas):
    """
    Get the schema definition for a specific property.
    Returns a list of possible schemas (for anyOf/oneOf cases).
    """
    if not isinstance(schema, dict):
        return []
    
    possible_schemas = []
    
    # Check direct properties
    if "properties" in schema and prop_name in schema["properties"]:
        prop_schema = schema["properties"][prop_name]
        possible_schemas.extend(extract_object_schemas(prop_schema, schemas))
    
    # Handle $ref at schema level
    if "$ref" in schema:
        ref_schema = resolve_ref(schema["$ref"], schemas)
        if ref_schema:
            possible_schemas.extend(get_property_schema(prop_name, ref_schema, schemas))
    
    return possible_schemas


def extract_object_schemas(field_schema, schemas):
    """
    Extract all possible object schemas from a field definition.
    Handles anyOf patterns where field can be object or IRI string.
    """
    if not isinstance(field_schema, dict):
        return []
    
    object_schemas = []
    
    # Direct $ref to another schema
    if "$ref" in field_schema:
        ref_schema = resolve_ref(field_schema["$ref"], schemas)
        if ref_schema:
            object_schemas.append(ref_schema)
    
    # Direct object with properties
    if field_schema.get("type") == "object" and "properties" in field_schema:
        object_schemas.append(field_schema)
    
    # Handle anyOf/oneOf - common pattern for "object or IRI"
    for keyword in ("anyOf", "oneOf"):
        if keyword in field_schema:
            for sub_schema in field_schema[keyword]:
                object_schemas.extend(extract_object_schemas(sub_schema, schemas))
    
    # Handle array items
    if "items" in field_schema:
        object_schemas.extend(extract_object_schemas(field_schema["items"], schemas))
    
    return object_schemas


def check_object(obj, schema, schemas, path=""):
    """
    Recursively check an object for undefined fields.
    Returns a list of (path, field_name) tuples for undefined fields.
    """
    undefined = []
    
    if not isinstance(obj, dict):
        return undefined
    
    allowed = get_allowed_properties(schema, schemas)
    
    for key, value in obj.items():
        current_path = f"{path}.{key}" if path else key
        
        # Check if this field is defined in schema
        if key not in allowed:
            undefined.append(current_path)
            continue
        
        # Recursively check nested objects
        if isinstance(value, dict):
            # Get possible schemas for this property
            prop_schemas = get_property_schema(key, schema, schemas)
            if prop_schemas:
                # Try each possible schema, use the one with fewest undefined fields
                best_undefined = None
                for prop_schema in prop_schemas:
                    nested_undefined = check_object(value, prop_schema, schemas, current_path)
                    if best_undefined is None or len(nested_undefined) < len(best_undefined):
                        best_undefined = nested_undefined
                if best_undefined:
                    undefined.extend(best_undefined)
        
        # Check arrays of objects
        elif isinstance(value, list):
            prop_schemas = get_property_schema(key, schema, schemas)
            for i, item in enumerate(value):
                if isinstance(item, dict) and prop_schemas:
                    item_path = f"{current_path}[{i}]"
                    best_undefined = None
                    for prop_schema in prop_schemas:
                        nested_undefined = check_object(item, prop_schema, schemas, item_path)
                        if best_undefined is None or len(nested_undefined) < len(best_undefined):
                            best_undefined = nested_undefined
                    if best_undefined:
                        undefined.extend(best_undefined)
    
    return undefined


def main():
    script_dir = Path(__file__).parent
    examples_dir = script_dir / "examples"
    
    schemas = load_schemas(script_dir)
    
    warnings = []
    checked = 0
    
    # Check every JSON in the examples/*/good/ directories
    for example_file in examples_dir.rglob("*.json"):
        rel_path = example_file.relative_to(examples_dir)
        parts = rel_path.parts
        
        if len(parts) < 3:
            continue
        
        schema_name = parts[0].lower()
        expected_result = parts[1]
        
        # Only check "good" examples - bad examples may intentionally have issues
        if expected_result != "good":
            continue
        
        if schema_name not in schemas:
            print(f"SKIP: No schema found for {schema_name} from {rel_path}")
            continue
        
        schema = schemas[schema_name]
        
        with open(example_file) as f:
            example = json.load(f)
        
        undefined = check_object(example, schema, schemas)
        checked += 1
        
        if undefined:
            print(f"WARN: {rel_path}")
            for field_path in undefined:
                print(f"  - undefined field: {field_path}")
            warnings.append((str(rel_path), undefined))
        else:
            print(f"OK: {rel_path}")
    
    print(f"\nChecked {checked} example(s)")
    
    if warnings:
        print(f"\n{len(warnings)} file(s) have undefined fields:")
        for file_path, fields in warnings:
            print(f"  {file_path}: {', '.join(fields)}")
        sys.exit(1)
    else:
        print("All examples use only defined fields")
        sys.exit(0)


if __name__ == "__main__":
    main()
