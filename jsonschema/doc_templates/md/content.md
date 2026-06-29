{#
    content is a template and not a macro in md
        because macro parameters are not through context
        when rendering a template from the macro  and it caused
        serious problems when using recursive calls
    mandatory context parameters:
    schema
#}
{# context parameters default values #}
{% set skip_headers = skip_headers or False %}
{% set depth = depth or 0 %}
{# end context parameters #}

{% set keys = schema.keywords %}
{%- if not skip_headers %}

{% if schema | should_render_title %}
**Title:** {{ schema.title }}
{% endif %}

{% set description = (schema | get_description) %}
{% include "section_description.md" %}
{% endif %}

{{ schema | md_type_info_table | md_render_key_value_details }}

{# Display examples #}
{% set examples = schema.examples %}
{% if examples %}
    {% include "section_examples.md" %}
{% endif %}

{# If this is a reference, do not expand inline #}
{% if schema.should_be_a_link(config) %}
    {# Only show the canonical link, not inline details #}
{% elif schema.refers_to -%}
    {# Only show the canonical link, not inline details #}
{% else %}
    {# Properties, pattern properties, additional properties #}
    {% if schema.is_object %}
        {{- schema | md_properties_table | md_generate_table -}}
    {% endif %}

    {# Combining: allOf, anyOf, oneOf, not #}
    {% if schema.kw_all_of %}
        {% with operator="allOf", title="All of", current_node=schema.kw_all_of, skip_required=True %}
            {% include "tabbed_section.md" %}
        {% endwith %}
    {% endif %}
    {% if schema.kw_any_of and not (schema | has_collapsed_nullable_branch) %}
        {% with operator="anyOf", title="Any of", current_node=schema.kw_any_of, skip_required=True %}
            {% include "tabbed_section.md" %}
        {% endwith %}
    {% endif %}
    {% if schema.kw_one_of and not (schema | has_collapsed_nullable_branch) %}
        {% with operator="oneOf", title="One of", current_node=schema.kw_one_of, skip_required=True %}
            {% include "tabbed_section.md" %}
        {% endwith %}
    {% endif %}
    {% if schema.kw_not %}
        {% include "section_not.md" %}
    {% endif %}

    {# Enum and const #}
    {% if schema.kw_enum -%}
        {% include "section_one_of.md" %}
    {%- endif %}
    {%- if schema.is_const -%}
        Specific value: `{{ schema.const_value | python_to_json }}`
    {%- endif -%}

    {# Conditional subschema, or if-then-else section #}
    {% if schema.has_conditional %}
        {% with skip_headers=False, depth=depth+1 %}
            {% include "section_conditional_subschema.md" %}
        {% endwith %}
    {% endif %}

    {# Required properties that are not defined under "properties". They will only be listed #}
    {% include "section_undocumented_required_properties.md" %}

    {# Show the requested type(s) #}
    {{- schema | md_restrictions_table | md_render_key_value_details -}}

    {# Show array restrictions #}
    {% if "array" in schema.type_name %}
        {% include "section_array.md" %}
    {% endif %}

    {# details of Properties, pattern properties, additional properties #}
    {% if schema.is_object %}
        {% include "section_properties_details.md" %}
    {% endif %}
{% endif %}

{# Placeholder for See Also section for main classes #}
{% if schema.title in ["Catalog", "Dataset", "Dataset Series", "Distribution"] %}
---
**See Also:** (related supporting classes)
{% endif %}
