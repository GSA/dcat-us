# Schema documentation

This directory contains Markdown documentation for the DCAT-US JSON schema.
The docs are generated with the `generate_schema_docs.py` script from the
parent directory. The docs are derived automatically from the JSON Schema
files without any manual intervention.

When you have made any changes to the schema files, run

```
poetry run python generate_schema_docs.py
```

in the parent directory to update the documentation here.

## Version controlling derived files

For convenience, we want these files to be under version control, but we
also want to ensure that they are up to date with any changes in the schema
files. We use a Github Actions script to run

```
poetry run generate_schema_docs.py --check
```

which validates that the documentation generated from the present version of
the schema matches precisely with what is in this directory.
