"""Generate documentation from the JSON schema files."""

import difflib
import filecmp
import glob
import json
import re
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


def _report_file_differences(comp_object):
    """Print the line differences for files in comp_object that differ."""
    for filename in comp_object.diff_files:
        print(f"\n=== {filename}")
        with open(Path(comp_object.left) / filename) as f_left:
            with open(Path(comp_object.right) / filename) as f_right:
                diff_list = difflib.unified_diff(f_left.readlines(), f_right.readlines())
                for line in diff_list:
                    print(line, end="")


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
            _report_file_differences(comparison)
            return 1
        else:
            return 0


def _wrapped_filter(old_filter, wrap_func):
    def _func_that_wraps(*args, **kwargs):
        return wrap_func(old_filter(*args, **kwargs))

    return _func_that_wraps


def _normalize_requirement_level(value):
    """Return a normalized requirement level label."""
    if not value:
        return "Optional"

    normalized = str(value).strip().lower()
    if normalized == "mandatory":
        return "Mandatory"
    if normalized == "recommended":
        return "Recommended"
    return "Optional"


def schema_requirement_level(schema):
    """Template helper for property requirement level.

    Prefer the top-level property keyword `requirementLevel`, with a fallback
    to legacy `_oldDocs.requirementLevel` for backward compatibility.
    """
    keywords = getattr(schema, "keywords", None) or {}

    if isinstance(keywords, dict):
        # New location for requirement metadata.
        if "requirementLevel" in keywords:
            return _normalize_requirement_level(keywords.get("requirementLevel"))

    old_docs = {}
    if isinstance(keywords, dict):
        old_docs_node = keywords.get("_oldDocs")
        if isinstance(old_docs_node, dict):
            old_docs = old_docs_node
        elif hasattr(old_docs_node, "keywords"):
            old_docs = {
                k: getattr(v, "literal", v) for k, v in old_docs_node.keywords.items()
            }
    return _normalize_requirement_level(old_docs.get("requirementLevel"))


def requirement_badge(schema):
    """Template helper that formats requirement level as an inline badge."""
    requirement = schema_requirement_level(schema)
    return f"[{requirement}]"


def properties_table_wrap(properties_list, schema):
    """Edit the properties list for our preferred format.

    properties_list is a list of lists that will eventually be formatted
    into a table.
    """
    for line in properties_list:
        if "Combination" in line:
            # replace combining with something better
            line[line.index("Combination")] = "More than one type"

    # remove lines
    def _remove_me(line):
        return (line[0].strip("*") == "Required" and line[1] == "No") or (
            all(not bool(item) for item in line)  # remove empty lines
        )

    return [line for line in properties_list if not _remove_me(line)]


def type_info_table_wrap(type_info_list):
    """Edit the type info table for our preferred format.

    type_info_list is a list of lists that will eventually be formatted
    into a table.
    """

    # edit lines
    for line in type_info_list:
        if line[0].strip("*") == "Defined in":
            # This is a link to another type, so turn it into a relative link
            match = re.match(r"^/dcat-us/3.0.0/definitions/(\w+)", line[1])
            class_name = match.group(1)
            line[1] = f"[{class_name.title()}](./{class_name.title()}.md)"
        elif "`combining`" in line:
            # replace combining with something better
            line[line.index("`combining`")] = "More than one type"

    # remove lines
    def _remove_me(line):
        return (line[0].strip("*") == "Required" and line[1] == "No") or (
            all(not bool(item) for item in line)  # remove empty lines
        )

    return [line for line in type_info_list if not _remove_me(line)]


def generate_docs(output_dir):
    """Generate the schema documentation into output_dir."""
    schema_files = sorted(glob.glob("definitions/*.json"))

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
        "link_to_reused_ref": True,
        "show_breadcrumbs": True,
        "show_toc": False,
        "template_name": "md",
        "custom_template_path": "doc_templates/md/content.md",
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

    # hack the rendering process
    original_md_properties_table = template_renderer.template.environment.filters[
        "md_properties_table"
    ]
    template_renderer.template.environment.filters["schema_requirement_level"] = (
        schema_requirement_level
    )
    template_renderer.template.environment.filters["requirement_badge"] = requirement_badge
    template_renderer.template.environment.filters["md_properties_table"] = (
        lambda schema: properties_table_wrap(
            original_md_properties_table(schema),
            schema,
        )
    )
    template_renderer.template.environment.filters["md_type_info_table"] = (
        _wrapped_filter(
            template_renderer.template.environment.filters["md_type_info_table"],
            type_info_table_wrap,
        )
    )

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
