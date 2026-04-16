# DCAT-US 3.0 JSON Schema

This directory contains JSON Schema definitions for validating DCAT-US 3.0 metadata.

## Structure

```
jsonschema/
├── Catalog.json                  # Root catalog schema
├── definitions/                  # Individual schema definitions
│   ├── AccessRestriction.json
│   ├── Activity.json
│   ├── Address.json
│   ├── Agent.json
│   ├── Attribution.json
│   ├── CatalogRecord.json
│   ├── Checksum.json
│   ├── Concept.json
│   ├── ConceptScheme.json
│   ├── CUIRestriction.json
│   ├── DataService.json
│   ├── Dataset.json
│   ├── DatasetSeries.json
│   ├── Distribution.json
│   ├── Document.json
│   ├── Identifier.json
│   ├── Kind.json
│   ├── Location.json
│   ├── Metric.json
│   ├── Organization.json
│   ├── PeriodOfTime.json
│   ├── QualityMeasurement.json
│   ├── Relationship.json
│   ├── Standard.json
│   └── UseRestriction.json
├── examples/                     # Test examples organized by schema
│   └── {SchemaName}/
│       ├── good/                 # Valid examples (should pass validation)
│       └── bad/                  # Invalid examples (should fail validation)
├── docs/                         # Generated markdown documentation
├── doc_templates/                # Templates for documentation generation
├── test_json_schema.py          # Validation test script
├── generate_schema_docs.py      # Documentation generator
├── parse_old_docs.py            # DCAT-US HTML documentation parser
├── check_missing_olddocs.py     # Check for missing oldDocs sections
├── check_undefined_fields.py    # Check for undefined fields in examples
├── create_null_examples.py      # Generate null-value test examples
├── pyproject.toml               # Python dependencies (Poetry)
└── package.json                 # Node.js dependencies (Prettier)
```

## Schema Definitions

The `definitions/` folder contains individual JSON Schema files for each DCAT-US class:

| Schema | Description |
|--------|-------------|
| AccessRestriction | Access restriction information (NARA) |
| Activity | Provenance activity |
| Address | Physical or mailing address |
| Agent | Entity responsible for resources |
| Attribution | Attribution information |
| CatalogRecord | Metadata about a catalog entry |
| Checksum | Checksum for data integrity |
| Concept | SKOS concept for controlled vocabularies |
| ConceptScheme | SKOS concept scheme |
| CUIRestriction | Controlled Unclassified Information restriction |
| DataService | API or service providing data access |
| Dataset | A dataset resource |
| DatasetSeries | A series of related datasets |
| Distribution | A specific representation of a dataset |
| Document | A document resource |
| Identifier | Identifier with scheme information |
| Kind | Contact information (vCard) |
| Location | Geographic location |
| Metric | Quality metric definition |
| Organization | An organization entity |
| PeriodOfTime | Temporal coverage |
| QualityMeasurement | Quality measurement result |
| Relationship | Relationship between resources |
| Standard | A standard or specification |
| UseRestriction | Use restriction information |

The root-level `Catalog.json` defines the collection of datasets.

## Setup

### Prerequisites

This project uses [Poetry](https://python-poetry.org/) for Python dependency management and Node.js for formatting tools.

**Python 3.13+** is required.

### Install Dependencies

```bash
# Install Python dependencies
poetry install

# Install Node.js dependencies (for Prettier)
npm ci
```

## Available Scripts

### Running Tests

Validate all example files against their schemas:

```bash
poetry run python test_json_schema.py
```

The script will output results for each example:

```
PASS: Agent/good/complete_example.json
PASS: Agent/bad/missing_required_name.json

All tests passed
```

### Generate Documentation

Generate markdown documentation from the JSON schema files:

```bash
# Generate docs
poetry run python generate_schema_docs.py

# Check if docs are up to date (useful for CI)
poetry run python generate_schema_docs.py --check
```

### Parse Old Documentation

Parse the DCAT-US HTML documentation and add `oldDocs` metadata to schemas:

```bash
# Preview changes without modifying files
poetry run python parse_old_docs.py --dry-run --verbose

# Apply changes
poetry run python parse_old_docs.py
```

### Check for Missing oldDocs

Report schema properties that don't have `oldDocs` sections:

```bash
poetry run python check_missing_olddocs.py
```

### Check for Undefined Fields

Validate that example files only use fields defined in their schemas:

```bash
poetry run python check_undefined_fields.py
```

### Generate Null Examples

Create test examples with `null` values for all non-required properties:

```bash
poetry run python create_null_examples.py
```

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

The schemas use JSON Schema 2020-12 draft. Here's an example using Python:

```python
import json
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

# Build a registry of all schema definitions
schema_dir = Path(".")
registry = Registry()

# Load Catalog.json
with open(schema_dir / "Catalog.json") as f:
    catalog_schema = json.load(f)
    registry = registry.with_resource(
        catalog_schema["$id"],
        Resource.from_contents(catalog_schema)
    )

# Load all definitions
for schema_file in (schema_dir / "definitions").glob("*.json"):
    with open(schema_file) as f:
        schema = json.load(f)
        registry = registry.with_resource(
            schema["$id"],
            Resource.from_contents(schema)
        )

# Create validator for Dataset
dataset_schema = json.load(open("definitions/Dataset.json"))
validator = Draft202012Validator(dataset_schema, registry=registry)

# Validate your data
data = {"@type": "Dataset", "title": "My Dataset", ...}
errors = list(validator.iter_errors(data))

if errors:
    for error in errors:
        print(f"Validation error: {error.message}")
else:
    print("Valid!")
```

See `test_json_schema.py` for a complete working example using the `jsonschema` and `referencing` libraries.

## Formatting

For consistency, we format all JSON schema files with [Prettier](https://prettier.io/). As a best practice, we check formatting in CI/CD and fail if files aren't formatted correctly.

Check formatting:

```bash
npx prettier --check definitions/*.json examples/
```

Apply formatting:

```bash
npx prettier --write definitions/*.json examples/
```

## Schema Metadata (oldDocs)

Each schema and property can include an `oldDocs` object containing metadata extracted from the [DCAT-US HTML documentation](https://infopolicy.github.io/dcat-us/). This includes:

- `rdfClass` / `uri` - The RDF class or property URI
- `definition` - The formal definition
- `usageNote` - Usage guidance
- `rationale` - Rationale for inclusion
- `requirementLevel` - Mandatory/Recommended/Optional
- `cardinality` - Allowed occurrences (e.g., `1..n`, `0..1`)
- `range` - Expected value type

To update `oldDocs` metadata from the latest HTML documentation:

```bash
poetry run python parse_old_docs.py
```

