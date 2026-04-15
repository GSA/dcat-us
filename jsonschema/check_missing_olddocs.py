#!/usr/bin/env python3
"""Check JSON schemas for properties missing oldDocs sections."""

import json
from pathlib import Path


def check_schema(schema_path: Path) -> list[str]:
    """Check a schema file and return list of properties missing oldDocs."""
    missing = []
    
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    
    # Check class-level oldDocs
    if 'oldDocs' not in schema:
        missing.append("(class-level)")
    
    # Check property-level oldDocs (skip JSON-LD structural fields)
    if 'properties' in schema:
        for prop_name, prop_def in schema['properties'].items():
            if prop_name in ('@id', '@type'):
                continue
            if isinstance(prop_def, dict) and 'oldDocs' not in prop_def:
                missing.append(prop_name)
    
    return missing


def main():
    schema_dir = Path(__file__).parent
    
    # Collect all schema files
    schema_files = [schema_dir / "Catalog.json"]
    schema_files.extend(sorted((schema_dir / "definitions").glob("*.json")))
    
    total_missing = 0
    
    for schema_path in schema_files:
        missing = check_schema(schema_path)
        if missing:
            print(f"\n{schema_path.name}:")
            for prop in missing:
                print(f"  - {prop}")
            total_missing += len(missing)
    
    print(f"\n{'=' * 40}")
    print(f"Total properties missing oldDocs: {total_missing}")


if __name__ == '__main__':
    main()
