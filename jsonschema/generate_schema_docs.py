"""Generate documentation from the JSON schema files."""

import filecmp
import glob
import json
import sys
import tempfile

from pathlib import Path
from urllib.parse import urlsplit

import click

from json_schema_for_humans import generate
from json_schema_for_humans.generation_configuration import get_final_config
from json_schema_for_humans.schema.schema_importer import get_schemas_to_render
from json_schema_for_humans.template_renderer import TemplateRenderer


def _any_differences(comp_object):
    """Check this directory and all of its subdirectories for differences.

    Argument is the output of a filecmp.dircmp call. Uses recursion and
    returns True if differences exist here or in any subdirectories.
    """
    if any(
        bool(getattr(comp_object, l))
        for l in [
            "diff_files",
            "left_only",
            "right_only",
            "common_funny",
            "funny_files",
        ]
    ):
        return True

    if any(_any_differences(subdir_cmp) for subdir_cmp in comp_object.subdirs):
        return True

    return False


def check_output_matches(output_dir):
    """Check if the generated files match the content already in output_dir.

    Return 0 if the files match and 1 if they don't.
    """
    # make a temporary directory to put our test output in:
    with tempfile.TemporaryDirectory() as d:
        generate_docs(d)
        comparison = filecmp.dircmp(
            d,
            Path(output_dir).absolute(),
            ignore=["README.md", "index.md"],
            shallow=False,
        )
        if _any_differences(comparison):
            comparison.report_full_closure()
            return 1
        else:
            return 0


def generate_docs(output_dir):
    """Generate the schema documentation into output_dir."""
    schema_files = ["Catalog.json"] + glob.glob("definitions/*.json")

    # We need to preload the schemas at their relative ids
    loaded_schemas = {}
    for schema_file in schema_files:
        with open(schema_file) as f:
            schema = json.load(f)
        # get path from $id
        _, _, path, _, _ = urlsplit(schema["$id"])
        loaded_schemas[path] = schema

    # generation config
    config = {
        "footer_show_time": False,  # so diff won't always be different
        "show_toc": False,
        "template_name": "md",
        "template_md_options": {
            "show_array_restrictions": False,
            "show_heading_numbers": False,
            "properties_table_columns": ["Property", "Type", "Title/Description"],
        },
    }
    final_config = get_final_config(True, True, True, True, config=config)

    schemas_to_render = []
    output_dir = Path(output_dir)
    for schema_file in schema_files:
        schemas_to_render += get_schemas_to_render(
            schema_file, output_dir, final_config.result_extension
        )
    template_renderer = TemplateRenderer(final_config)
    generate.generate_schemas_doc(schemas_to_render, template_renderer, loaded_schemas)
    generate.copy_additional_files_to_target(schemas_to_render, final_config)


@click.command()
@click.option("-o", "--output-dir", help="Output directory", default="docs")
@click.option(
    "--check", help="Check if the output matches the output directory", is_flag=True
)
def main(output_dir="docs", check=True):
    """Generate schema documentation."""

    if check:
        sys.exit(check_output_matches(output_dir))

    generate_docs(output_dir)


if __name__ == "__main__":
    main()
