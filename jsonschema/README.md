# DCAT-US 3.0 JSON Schema

This directory contains JSON Schema definitions for validating DCAT-US 3.0 metadata.

## Structure

```
jsonschema/
├── dcat_us_3.0.0_schema.json    # Main schema with all definitions referenced
├── definitions/                  # Individual schema definitions
│   ├── Agent.json
│   ├── Catalog.json
│   ├── Dataset.json
│   ├── Distribution.json
│   └── ...
├── examples/                     # Test examples organized by schema
│   └── {SchemaName}/
│       ├── good/                 # Valid examples (should pass validation)
│       └── bad/                  # Invalid examples (should fail validation)
└── test_json_schema.py          # Validation test script
```

## Schema Definitions

The `definitions/` folder contains individual JSON Schema files for each DCAT-US class:

| Schema | Description |
|--------|-------------|
| AccessRestriction | Access restriction information |
| Activity | Provenance activity |
| Address | Physical or mailing address |
| Agent | Entity responsible for resources |
| Attribution | Attribution information |
| Catalog | Collection of datasets |
| CatalogRecord | Metadata about a catalog entry |
| Checksum | Checksum for data integrity |
| Concept | SKOS concept for controlled vocabularies |
| ConceptScheme | SKOS concept scheme |
| DataService | API or service providing data access |
| Dataset | A dataset resource |
| DatasetSeries | A series of related datasets |
| Distribution | A specific representation of a dataset |
| Document | A document resource |
| Identifier | Identifier with scheme information |
| Kind | Contact information (vCard) |
| LiabilityStatement | Liability disclaimer |
| LicenseDocument | License information |
| Location | Geographic location |
| MediaType | IANA media type |
| Metric | Quality metric definition |
| Organization | An organization entity |
| PeriodOfTime | Temporal coverage |
| Person | A person entity |
| ProvenanceStatement | Provenance information |
| QualityMeasurement | Quality measurement result |
| Relationship | Relationship between resources |
| RightsStatement | Rights information |
| Standard | A standard or specification |
| UseRestriction | Use restriction information |

## Running Tests

### Prerequisites

Install the required Python package:

```bash
pip install jsonschema
```

### Execute Tests

```bash
cd jsonschema
python test_json_schema.py
```

The script will output results for each example:

```
PASS: Agent/good/complete_example.json
PASS: Agent/bad/missing_required_name.json

All tests passed
```

If any test fails unexpectedly, the script exits with code 1.

## Adding New Test Examples

To add test examples for a schema:

1. Create the directory structure under `examples/`:
   ```
   examples/{SchemaName}/good/
   examples/{SchemaName}/bad/
   ```

2. Add valid JSON examples to the `good/` folder. These should pass schema validation.

3. Add invalid JSON examples to the `bad/` folder. These should fail schema validation (e.g., missing required fields, wrong types).

### Example Structure

For the `Agent` schema:

```
examples/Agent/
├── good/
│   └── complete_example.json    # Valid Agent with all fields
└── bad/
    └── missing_required_name.json  # Missing required "name" field
```

### Naming Conventions

- Use descriptive names that indicate what the example tests
- For bad examples, name should indicate the validation issue (e.g., `missing_required_name.json`, `invalid_type.json`)

## Integration

### Validating Data Programmatically

```python
import json
from jsonschema import Draft7Validator

# Load the main schema
with open("dcat_us_3.0.0_schema.json") as f:
    schema = json.load(f)

# Create validator
validator = Draft7Validator(schema)

# Validate your data
data = {"@type": "Dataset", "title": "My Dataset", ...}
errors = list(validator.iter_errors(data))

if errors:
    for error in errors:
        print(f"Validation error: {error.message}")
else:
    print("Valid!")
```

### Using Individual Definitions

When using individual definition files, note that cross-references (e.g., `$ref: "#/definitions/Concept"`) require all definitions to be loaded together. The test script demonstrates how to combine definitions into a single schema for validation.
