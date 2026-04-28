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


MAIN_CLASS_PAGES = [
    {
        "source": "Catalog.md",
        "output": "catalog.md",
        "title": "Catalog",
        "intro": "The catalog of datasets, services, and other information describing data assets.",
    },
    {
        "source": "Dataset.md",
        "output": "dataset.md",
        "title": "Dataset",
        "intro": "Information about a dataset, including identifiers, contacts, coverage, distributions, and related resources.",
    },
    {
        "source": "DatasetSeries.md",
        "output": "dataset-series.md",
        "title": "Dataset Series",
        "intro": "Information about a dataset series, including its members, ordering, coverage, and publishing details.",
    },
    {
        "source": "Distribution.md",
        "output": "distribution.md",
        "title": "Distribution",
        "intro": "Information about a distribution, including access methods, formats, licenses, restrictions, and quality details.",
    },
]

GROUPED_CLASS_PAGES = [
    {
        "output": "agents.md",
        "title": "Agents",
        "intro": "Data information classes including Agent, Organization, and Kind, which describe organizations, people, and contact information.",
        "classes": ["Agent.md", "Organization.md", "Kind.md"],
    },
    {
        "output": "constraints-and-restrictions.md",
        "title": "Constraints and Restrictions",
        "intro": "Restriction classes describing access limits, controlled unclassified information, and rules on how a resource may be used.",
        "classes": ["AccessRestriction.md", "CUIRestriction.md", "UseRestriction.md"],
    },
    {
        "output": "identifiers-and-relationships.md",
        "title": "Identifiers and Relationships",
        "intro": "Supporting classes for identifiers, relationships, checksums, and controlled concepts used to describe and connect resources.",
        "classes": [
            "Identifier.md",
            "Relationship.md",
            "Checksum.md",
            "Concept.md",
            "ConceptScheme.md",
        ],
    },
    {
        "output": "temporal-spatial-metrics.md",
        "title": "Temporal, Spatial, and Metrics",
        "intro": "Supporting classes for time periods, locations, quality metrics, measurements, activities, and addresses.",
        "classes": [
            "PeriodOfTime.md",
            "Location.md",
            "Metric.md",
            "QualityMeasurement.md",
            "Activity.md",
            "Address.md",
        ],
    },
    {
        "output": "quality-governance.md",
        "title": "Quality and Governance",
        "intro": "Supporting classes for standards, documents, catalog records, data services, and attribution used in governance and quality description.",
        "classes": [
            "Standard.md",
            "Document.md",
            "CatalogRecord.md",
            "DataService.md",
            "Attribution.md",
        ],
    },
]


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


def _class_name_from_file(file_name):
    return Path(file_name).stem


def _class_anchor(class_name):
    slug = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1-\2", class_name)
    slug = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", slug)
    return slug.lower()


def _build_class_link_map():
    link_map = {}

    for page in MAIN_CLASS_PAGES:
        class_name = _class_name_from_file(page["source"])
        target = f"./{page['output']}#root"
        link_map[class_name.lower()] = target

    for page in GROUPED_CLASS_PAGES:
        for class_file in page["classes"]:
            class_name = _class_name_from_file(class_file)
            target = f"./{page['output']}#{_class_anchor(class_name)}"
            link_map[class_name.lower()] = target

    return link_map


CLASS_LINK_MAP = _build_class_link_map()
CLASS_DISPLAY_NAME_MAP = {
    _class_name_from_file(page["source"]).lower(): _class_name_from_file(page["source"])
    for page in MAIN_CLASS_PAGES
}
CLASS_DISPLAY_NAME_MAP.update(
    {
        _class_name_from_file(class_file).lower(): _class_name_from_file(class_file)
        for page in GROUPED_CLASS_PAGES
        for class_file in page["classes"]
    }
)


def _canonical_class_doc_link(schema_node):
    if schema_node is None:
        return None

    candidates = [schema_node, schema_node.refers_to, schema_node.refers_to_merged]
    for candidate in candidates:
        if candidate is None:
            continue

        class_name = None
        if getattr(candidate, "ref_path", None):
            class_name = candidate.ref_path.split("/")[-1]
        elif getattr(candidate, "definition_name", None):
            class_name = candidate.definition_name

        if not class_name:
            continue

        normalized_name = class_name.lower()
        target = CLASS_LINK_MAP.get(normalized_name)
        if target:
            display_name = CLASS_DISPLAY_NAME_MAP.get(normalized_name, class_name)
            return f"[{display_name}]({target})"

    return None


def _rewrite_class_doc_links(content):
    def _replace(match):
        label = match.group(1)
        basename = match.group(2).lower()
        target = CLASS_LINK_MAP.get(basename)
        if target is None:
            return match.group(0)
        return f"[{label}]({target})"

    return re.sub(r"\[([^\]]+)\]\(\./([A-Za-z0-9]+)\.md\)", _replace, content)


def _rewrite_local_anchors(content, anchor_prefix="", root_anchor="root"):
    def _replace_anchor(match):
        anchor_name = match.group(1)
        if anchor_name == "root":
            return f'<a name="{root_anchor}"></a>'
        return f'<a name="{anchor_prefix}{anchor_name}"></a>'

    def _replace_fragment(match):
        anchor_name = match.group(1).strip()
        if anchor_name == "root":
            return f"](#{root_anchor})"
        return f"](#{anchor_prefix}{anchor_name})"

    content = re.sub(r'<a name="([^"]+)"></a>', _replace_anchor, content)
    return re.sub(r"\]\(#([^\)]+?)\s*\)", _replace_fragment, content)


def _add_heading_anchor_links(content):
    lines = content.splitlines()

    for index, line in enumerate(lines):
        inline_match = re.match(r'^(#{1,6}) <a name="([^"]+)"></a>(.+)$', line)
        if inline_match:
            heading_marks, anchor_name, heading_text = inline_match.groups()
            if f'](#{anchor_name})' not in heading_text:
                lines[index] = (
                    f'{heading_marks} <a name="{anchor_name}"></a>'
                    f'{heading_text} [#](#{anchor_name})'
                )
            continue

        anchor_match = re.match(r'^<a name="([^"]+)"></a>$', line)
        if not anchor_match:
            continue

        anchor_name = anchor_match.group(1)
        next_index = index + 1
        while next_index < len(lines) and not lines[next_index].strip():
            next_index += 1

        if next_index >= len(lines):
            continue

        heading_match = re.match(r'^(#{1,6}) (.+)$', lines[next_index])
        if heading_match and f'](#{anchor_name})' not in lines[next_index]:
            heading_marks, heading_text = heading_match.groups()
            lines[next_index] = f'{heading_marks} {heading_text} [#](#{anchor_name})'

    return "\n".join(lines)


def _rewrite_unresolved_self_item_links(content, page_title):
    anchors = set(re.findall(r'<a name="([^"]+)"></a>', content))
    self_labels = {page_title, f"DCAT-US 3 {page_title}"}

    def _replace(match):
        label = match.group(1)
        fragment = match.group(2)
        if fragment in anchors:
            return match.group(0)
        if fragment.endswith("_items") and label in self_labels:
            return f"[{label}](#root)"
        return match.group(0)

    return re.sub(r'\[([^\]]+)\]\(#([^\)]+)\)', _replace, content)


def _normalize_doc_content(content, anchor_prefix="", root_anchor="root"):
    content = content.strip()
    content = _rewrite_class_doc_links(content)
    content = _rewrite_local_anchors(
        content,
        anchor_prefix=anchor_prefix,
        root_anchor=root_anchor,
    )
    return _add_heading_anchor_links(content)


def _write_text(output_path, content):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f"{content.rstrip()}\n", encoding="utf-8")


def _read_generated_doc(docs_dir, file_name):
    path = Path(docs_dir) / file_name
    return path.read_text(encoding="utf-8")


def _clear_generated_markdown(output_dir):
    for markdown_file in Path(output_dir).glob("*.md"):
        if markdown_file.name == "README.md":
            continue
        markdown_file.unlink()


def _build_public_docs(rendered_docs_dir, output_dir):
    output_dir = Path(output_dir)
    _clear_generated_markdown(output_dir)

    for page in MAIN_CLASS_PAGES:
        raw_content = _read_generated_doc(rendered_docs_dir, page["source"])
        page_content = _normalize_doc_content(raw_content, root_anchor="root")
        page_content = _rewrite_unresolved_self_item_links(page_content, page["title"])
        page_content = f'<a name="root"></a>\n\n{page["intro"]}\n\n{page_content}'
        _write_text(output_dir / page["output"], page_content)

    for page in GROUPED_CLASS_PAGES:
        sections = []
        for class_file in page["classes"]:
            class_name = _class_name_from_file(class_file)
            section_anchor = _class_anchor(class_name)
            raw_content = _read_generated_doc(rendered_docs_dir, class_file)
            section_content = _normalize_doc_content(
                raw_content,
                anchor_prefix=f"{section_anchor}--",
                root_anchor=section_anchor,
            )
            sections.append(
                f'<a name="{section_anchor}"></a>\n\n## Class {class_name} [#](#{section_anchor})\n\n{section_content}'
            )

        page_content = "\n\n---\n\n".join(sections)
        _write_text(
            output_dir / page["output"],
            f"# {page['title']}\n\n{page['intro']}\n\n{page_content}",
        )


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


def _normalize_label(value):
    if value is None:
        return ""
    return re.sub(r"[^a-z0-9]+", "", str(value).strip().lower())


def _escape_for_table(value):
    if value is None:
        return ""
    return str(value).translate(str.maketrans({"|": "\\|", "`": "\\`", "\n": "<br />"}))


def should_render_title(schema):
    """Return False when the title just repeats the current node label."""
    title = getattr(schema, "title", None)
    normalized_title = _normalize_label(title)
    if not normalized_title:
        return False

    candidate_labels = {
        _normalize_label(getattr(schema, "property_name", None)),
        _normalize_label(getattr(schema, "name_for_breadcrumbs", None)),
    }
    candidate_labels.discard("")
    return normalized_title not in candidate_labels


def property_summary_text(schema):
    """Return the preferred summary text for property tables."""
    description = getattr(schema, "description", None)
    if description:
        return description

    title = getattr(schema, "title", None)
    if should_render_title(schema):
        return title

    return ""


def _array_item_type_label(item_schema):
    canonical_link = _canonical_class_doc_link(item_schema)
    if canonical_link:
        return f"{canonical_link} classes"

    title = getattr(item_schema, "title", None)
    if should_render_title(item_schema):
        return title

    return getattr(item_schema, "type_name", "item")


def _display_type_label(schema):
    array_item = getattr(schema, "array_items_def", None)
    tuple_items = getattr(schema, "tuple_validation_items", None) or []
    if array_item and not tuple_items:
        label = f"array of {_array_item_type_label(array_item)}"
        if "null" in str(getattr(schema, "type_name", "")).lower():
            return f"null or {label}"
        return label

    return None


def schema_requirement_level(schema):
    """Template helper for property requirement level.

    Prefer the top-level property keyword `requirementLevel`, with a fallback
    to legacy `_oldDocs.requirementLevel` for backward compatibility.
    """
    keywords = getattr(schema, "keywords", None) or {}

    if isinstance(keywords, dict):
        # New location for requirement metadata.
        if "requirementLevel" in keywords:
            requirement_level = keywords.get("requirementLevel")
            if hasattr(requirement_level, "literal"):
                requirement_level = requirement_level.literal
            return _normalize_requirement_level(requirement_level)

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


def properties_table_wrap(properties_list, schema):
    """Edit the properties list for our preferred format.

    properties_list is a list of lists that will eventually be formatted
    into a table.
    """
    property_nodes = list(schema.iterate_properties)

    for index, line in enumerate(properties_list):
        if "Combination" in line:
            # replace combining with something better
            line[line.index("Combination")] = "More than one type"

        if not line:
            continue

        if index == 0:
            line = list(line)
            properties_list[index] = line
            property_column_index = line.index("Property")
            line.insert(property_column_index + 2, "Requirement Level")
            continue

        property_column_index = 0
        if line[property_column_index].startswith(("+ ", "- ")):
            line[property_column_index] = line[property_column_index][2:]

        property_node = property_nodes[index - 1]
        display_type = _display_type_label(property_node)
        if display_type:
            line[property_column_index + 1] = display_type
        requirement = schema_requirement_level(property_node)
        line.insert(property_column_index + 2, requirement)
        line[property_column_index + 3] = _escape_for_table(
            property_summary_text(property_node)
        )

    # remove lines
    def _remove_me(line):
        return (line[0].strip("*") == "Required" and line[1] == "No") or (
            all(not bool(item) for item in line)  # remove empty lines
        )

    return [line for line in properties_list if not _remove_me(line)]


def array_items_restrictions_wrap(items_restrictions, schema):
    if not items_restrictions:
        return items_restrictions

    items = ([schema.array_items_def] if schema.array_items_def else []) + schema.tuple_validation_items
    for row, item in zip(items_restrictions[1:], items):
        canonical_link = _canonical_class_doc_link(item)
        if canonical_link:
            row[0] = canonical_link
            continue

        item_title = getattr(item, "title", None)
        schema_title = getattr(schema, "title", None)
        if item_title and schema_title and item_title == schema_title:
            row[0] = f"[{item_title}](#root)"

    return items_restrictions


def type_info_table_wrap(type_info_list, schema):
    """Edit the type info table for our preferred format.

    type_info_list is a list of lists that will eventually be formatted
    into a table.
    """

    canonical_link = _canonical_class_doc_link(schema)

    # edit lines
    for line in type_info_list:
        line_label = line[0].strip("*")
        if line_label == "Type":
            display_type = _display_type_label(schema)
            if display_type:
                line[1] = display_type
        elif line_label == "Defined in":
            if canonical_link:
                line[1] = canonical_link
            else:
                # This is a link to another type, so turn it into a relative link
                match = re.match(r"^/dcat-us/3.0.0/definitions/(\w+)", line[1])
                class_name = match.group(1)
                line[1] = f"[{class_name.title()}](./{class_name.title()}.md)"
        elif line_label == "Same definition as" and canonical_link:
            line[1] = canonical_link
        elif "`combining`" in line:
            # replace combining with something better
            line[line.index("`combining`")] = "More than one type"

    # remove lines
    def _remove_me(line):
        return (line[0].strip("*") == "Required" and line[1] == "No") or (
            all(not bool(item) for item in line)  # remove empty lines
        )

    return [line for line in type_info_list if not _remove_me(line)]


def _render_raw_docs(output_dir):
    """Generate the unmerged schema documentation into output_dir."""
    schema_files = sorted(glob.glob("definitions/*.json"))

    loaded_schemas = {}
    for schema_file in schema_files:
        with open(schema_file) as f:
            schema = json.load(f)
        _, _, path, _, _ = urlsplit(schema["$id"])
        loaded_schemas[path] = schema

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

    original_md_properties_table = template_renderer.template.environment.filters[
        "md_properties_table"
    ]
    template_renderer.template.environment.filters["should_render_title"] = (
        should_render_title
    )
    template_renderer.template.environment.filters["schema_requirement_level"] = (
        schema_requirement_level
    )
    template_renderer.template.environment.filters["md_properties_table"] = (
        lambda schema: properties_table_wrap(
            original_md_properties_table(schema),
            schema,
        )
    )
    original_md_array_items_restrictions = template_renderer.template.environment.filters[
        "md_array_items_restrictions"
    ]
    original_md_type_info_table = template_renderer.template.environment.filters[
        "md_type_info_table"
    ]
    template_renderer.template.environment.filters["canonical_class_doc_link"] = (
        _canonical_class_doc_link
    )
    template_renderer.template.environment.filters["md_array_items_restrictions"] = (
        lambda schema: array_items_restrictions_wrap(
            original_md_array_items_restrictions(schema),
            schema,
        )
    )
    template_renderer.template.environment.filters["md_type_info_table"] = (
        lambda schema: type_info_table_wrap(
            original_md_type_info_table(schema),
            schema,
        )
    )

    generate.generate_schemas_doc(schemas_to_render, template_renderer, loaded_schemas)
    generate.copy_additional_files_to_target(schemas_to_render, final_config)


def generate_docs(output_dir):
    """Generate the schema documentation into output_dir."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        _render_raw_docs(temp_path)
        _build_public_docs(temp_path, output_dir)


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
