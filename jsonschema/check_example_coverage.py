#!/usr/bin/env python3
"""
Check that good/typical examples include all Mandatory and Recommended fields.

This script analyzes JSON schema files for properties with _oldDocs.requirementLevel
set to "Mandatory" or "Recommended", then verifies that the corresponding
good example files include those fields.

Usage:
    poetry run python check_example_coverage.py           # Check all schemas
    poetry run python check_example_coverage.py --verbose # Show all fields per schema
"""

import argparse
import json
from pathlib import Path


def get_required_fields(schema: dict) -> tuple[list[str], list[str]]:
    """Extract Mandatory and Recommended fields from schema based on _oldDocs."""
    mandatory = []
    recommended = []
    
    properties = schema.get('properties', {})
    for prop_name, prop_def in properties.items():
        # Skip JSON-LD structural fields
        if prop_name in ('@id', '@type'):
            continue
            
        if not isinstance(prop_def, dict):
            continue
            
        old_docs = prop_def.get('_oldDocs', {})
        req_level = old_docs.get('requirementLevel', '')
        
        if 'Mandatory' in req_level:
            mandatory.append(prop_name)
        elif 'Recommended' in req_level:
            recommended.append(prop_name)
    
    return mandatory, recommended


def check_example_coverage(example_path: Path, mandatory: list[str], recommended: list[str]) -> dict:
    """Check which required fields are present in an example."""
    with open(example_path, 'r', encoding='utf-8') as f:
        example = json.load(f)
    
    # Get all keys in the example (handle both single object and array)
    if isinstance(example, list):
        example_keys = set()
        for item in example:
            if isinstance(item, dict):
                example_keys.update(item.keys())
    else:
        example_keys = set(example.keys())
    
    missing_mandatory = [f for f in mandatory if f not in example_keys]
    missing_recommended = [f for f in recommended if f not in example_keys]
    present_mandatory = [f for f in mandatory if f in example_keys]
    present_recommended = [f for f in recommended if f in example_keys]
    
    return {
        'missing_mandatory': missing_mandatory,
        'missing_recommended': missing_recommended,
        'present_mandatory': present_mandatory,
        'present_recommended': present_recommended,
    }


def find_typical_example(examples_dir: Path) -> Path | None:
    """Find the typical/complete good example for a schema."""
    good_dir = examples_dir / 'good'
    if not good_dir.exists():
        return None
    
    # Look for typical example first, then any good example
    for pattern in ['typical*.json', 'complete*.json', '*.json']:
        examples = list(good_dir.glob(pattern))
        if examples:
            return examples[0]
    
    return None


def main():
    parser = argparse.ArgumentParser(description='Check example coverage of Mandatory/Recommended fields')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show all fields per schema')
    args = parser.parse_args()
    
    schema_dir = Path(__file__).parent
    examples_dir = schema_dir / 'examples'
    
    # Collect all schemas from definitions directory
    schemas = {}
    for schema_file in (schema_dir / 'definitions').glob('*.json'):
        schemas[schema_file.stem] = schema_file
    
    total_issues = 0
    schemas_checked = 0
    schemas_with_reqs = 0
    
    for schema_name, schema_path in sorted(schemas.items()):
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)
        
        mandatory, recommended = get_required_fields(schema)
        
        # Skip schemas with no mandatory/recommended fields
        if not mandatory and not recommended:
            continue
        
        schemas_with_reqs += 1
        
        # Find typical example
        schema_examples_dir = examples_dir / schema_name
        typical_example = find_typical_example(schema_examples_dir)
        
        if not typical_example:
            print(f"\n{schema_name}: No good example found")
            print(f"  Mandatory fields: {mandatory}")
            print(f"  Recommended fields: {recommended}")
            total_issues += len(mandatory) + len(recommended)
            continue
        
        schemas_checked += 1
        coverage = check_example_coverage(typical_example, mandatory, recommended)
        
        has_issues = coverage['missing_mandatory'] or coverage['missing_recommended']
        
        if has_issues or args.verbose:
            print(f"\n{schema_name} ({typical_example.name}):")
            
            if args.verbose:
                if coverage['present_mandatory']:
                    print(f"  ✓ Mandatory present: {coverage['present_mandatory']}")
                if coverage['present_recommended']:
                    print(f"  ✓ Recommended present: {coverage['present_recommended']}")
            
            if coverage['missing_mandatory']:
                print(f"  ✗ Missing MANDATORY: {coverage['missing_mandatory']}")
                total_issues += len(coverage['missing_mandatory'])
            if coverage['missing_recommended']:
                print(f"  ✗ Missing Recommended: {coverage['missing_recommended']}")
                total_issues += len(coverage['missing_recommended'])
    
    print(f"\n{'=' * 50}")
    print(f"Schemas with Mandatory/Recommended fields: {schemas_with_reqs}")
    print(f"Schemas with good examples: {schemas_checked}")
    print(f"Total missing fields: {total_issues}")
    
    if total_issues == 0:
        print("\n✓ All typical examples cover Mandatory and Recommended fields!")
    
    return 0 if total_issues == 0 else 1


if __name__ == '__main__':
    exit(main())
