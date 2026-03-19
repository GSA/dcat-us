"""Generate documentation from the JSON schema files."""

import glob
import json

from pathlib import Path
from urllib.parse import urlsplit

from json_schema_for_humans import generate
from json_schema_for_humans.generation_configuration import get_final_config
from json_schema_for_humans.schema.schema_importer import get_schemas_to_render
from json_schema_for_humans.template_renderer import TemplateRenderer


def main():
    """Generate schema documentation."""

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
            "show_toc": False,
            "template_name": "md",
    }
    final_config = get_final_config(True, True, True, True, config=config)

    schemas_to_render = []
    output_dir = Path(__file__).parent / "docs/"
    for schema_file in schema_files:
        schemas_to_render += get_schemas_to_render(schema_file,
                                                   output_dir,
                                                   final_config.result_extension)
    template_renderer = TemplateRenderer(final_config)
    generate.generate_schemas_doc(schemas_to_render, template_renderer, loaded_schemas)
    generate.copy_additional_files_to_target(schemas_to_render, final_config)


if __name__ == "__main__":
    main()
