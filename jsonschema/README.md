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
├── parse_old_docs.py            # Historical one-time DCAT-US HTML metadata import
├── check_missing_olddocs.py     # Check for missing oldDocs sections
├── check_requirement_levels.py  # Check/fix oldDocs requirement levels
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

### Install Poetry

If Poetry is not already installed, use one of the following methods:

```bash
# Recommended
pipx install poetry

# Alternative installer from poetry.org
curl -sSL https://install.python-poetry.org | python3 -
```

Verify installation:

```bash
poetry --version
```

### Configure Poetry Environment

From this `jsonschema/` directory:

```bash
# Ensure Poetry uses Python 3.13+
poetry env use python3.13

# Confirm selected interpreter and virtual environment
poetry env info
```

### Install Dependencies

```bash
# Install Python dependencies
poetry install

# Install Node.js dependencies (for Prettier)
npm ci
```

## Available Scripts

All repository scripts are listed below with a brief summary and usage.

### test_json_schema.py

Summary: Validates all `examples/{Class}/good` (must pass) and `examples/{Class}/bad` (must fail) against the schema registry.

```bash
poetry run python test_json_schema.py
```

### generate_schema_docs.py

Summary: Generates Markdown schema documentation in `docs/` from the JSON Schema files.

```bash
# Generate docs
poetry run python generate_schema_docs.py

# Check if generated docs are up to date (CI-friendly)
poetry run python generate_schema_docs.py --check

# Show CLI help
poetry run python generate_schema_docs.py --help
```

### parse_old_docs.py

Summary: Historical bootstrap script that imported `oldDocs` metadata from the legacy DCAT-US HTML documentation.

Note: This was effectively a one-time import step. The imported metadata was manually corrected and refined in this repository afterward, so re-running the parser is not a meaningful validation step and its output should not be used as a test oracle.

For ongoing validation of `oldDocs`, use:

- `poetry run python check_missing_olddocs.py`
- `poetry run python check_requirement_levels.py`
- `poetry run python check_example_coverage.py`

```bash
# Historical preview only
poetry run python parse_old_docs.py --dry-run --verbose

# Historical import/apply mode
poetry run python parse_old_docs.py

# Show CLI help
poetry run python parse_old_docs.py --help
```

### check_missing_olddocs.py

Summary: Reports schema properties missing `oldDocs` metadata.

```bash
poetry run python check_missing_olddocs.py
```

Note: This script does not expose a dedicated `--help` interface; running it executes the check.

### check_requirement_levels.py

Summary: Compares `oldDocs.requirementLevel` against schema `required` fields and optionally fixes mismatches.

```bash
# Report mismatches
poetry run python check_requirement_levels.py

# Apply automatic fixes
poetry run python check_requirement_levels.py --fix

# Show CLI help
poetry run python check_requirement_levels.py --help
```

### check_undefined_fields.py

Summary: Verifies that example JSON files only use fields defined by their schema.

```bash
poetry run python check_undefined_fields.py
```

Note: This script does not expose a dedicated `--help` interface; running it executes the check.

### create_null_examples.py

Summary: Generates `null_example.json` files with required starter fields plus nullable optional fields.

```bash
poetry run python create_null_examples.py
```

Note: This script does not support `--help`; passing flags will still run generation logic.

### check_example_coverage.py

Summary: Checks whether good typical/complete examples include fields marked Mandatory or Recommended in `oldDocs`.

```bash
# Coverage check
poetry run python check_example_coverage.py

# Verbose output
poetry run python check_example_coverage.py --verbose

# Show CLI help
poetry run python check_example_coverage.py --help
```

### add_schema_examples.py

Summary: Populates schema-level and property-level examples in `definitions/*.json` from `examples/{Class}/good/typical_example.json` and `examples/{Class}/good/complete_example.json`.

- Class-level `examples`: uses values from `typical_example.json`.
- Property-level `examples`: combines values from both typical and complete examples.
- `examples` arrays are rewritten from source files each run (idempotent and deterministic).

```bash
# Apply updates to schema definitions
poetry run python add_schema_examples.py

# Preview what would be updated without writing files
poetry run python add_schema_examples.py --dry-run
```

Typical workflow:

```bash
poetry run python add_schema_examples.py
npx prettier --write definitions/*.json
poetry run python generate_schema_docs.py
```

### Script Help Verification

The following commands were tested in this repository using Poetry:

- `poetry run python generate_schema_docs.py --help` (works)
- `poetry run python parse_old_docs.py --help` (works; historical/bootstrap script, not part of routine validation)
- `poetry run python check_requirement_levels.py --help` (works)
- `poetry run python check_example_coverage.py --help` (works)
- `poetry run python check_missing_olddocs.py --help` (no help interface; runs check)
- `poetry run python check_undefined_fields.py --help` (no help interface; runs check)
- `poetry run python create_null_examples.py --help` (not supported; script executes)
- `poetry run python test_json_schema.py --help` (not supported; script executes test suite)

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

The repository originally seeded `oldDocs` metadata from the legacy DCAT-US HTML documentation using `parse_old_docs.py`. That import was a one-time bootstrap step, and the resulting metadata has since been manually updated in places.

Because of that, `parse_old_docs.py` should not be treated as a regression test or as a source of truth for current schema metadata. A dry run is expected to report differences.

For current validation, use:

- `poetry run python check_missing_olddocs.py`
- `poetry run python check_requirement_levels.py`
- `poetry run python check_example_coverage.py`

If you need to inspect the historical importer behavior, you can still run:

```bash
poetry run python parse_old_docs.py
```

