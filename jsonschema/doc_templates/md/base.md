{% set depth = 0 %}
{{ schema.keywords.get("title").literal | default("Schema Docs") | md_heading(depth) }}
{% set contentBase %}
{% with schema=schema, skip_headers=False, depth=depth %}
    {% include "content.md" %}
{% endwith %}
{% endset %}

{{ md_get_toc() }}

{{ contentBase }}
