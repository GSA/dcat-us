
{{ schema | md_array_restrictions | md_generate_table }}

{# Only show array items table; suppress inline details if canonical link exists #}
{% if schema.array_items_def or schema.tuple_validation_items %}
{{ schema | md_array_items_restrictions | md_generate_table }}
{% endif %}

{# Only expand inline details for array items if not a reference/canonical link #}
{% if schema.array_items_def %}
    {% set is_linked_array_item = schema.array_items_def.should_be_a_link(config) or schema.array_items_def.refers_to %}
    {% if not is_linked_array_item %}
        {% filter md_heading(depth+1, schema.array_items_def.html_id) %}
            {{ schema.array_items_def.title or 'Array Item' }}
        {% endfilter %}
        {% with schema=schema.array_items_def, skip_headers=False, depth=depth+1, skip_required=True %}
            {% include "content.md" %}
        {% endwith %}
    {% endif %}
{% endif %}

{# Tuple validation items: only expand if not a reference #}
{% if schema.tuple_validation_items %}
    {% for item in schema.tuple_validation_items %}
        {% set is_linked_tuple_item = item.should_be_a_link(config) or item.refers_to %}
        {% if not is_linked_tuple_item %}
            {% filter md_heading(depth+1) %}
                {{ item.title or 'Tuple Item' }}
            {% endfilter %}
            {% with schema=item, skip_headers=False, depth=depth+1, skip_required=True %}
                {% include "content.md" %}
            {% endwith %}
        {% endif %}
    {% endfor %}
{% endif %}

{# Contains/Additional items unchanged for now #}
{% if schema.kw_contains and schema.kw_contains.literal != {} %}
    {{ "At least one of the items must be" | md_heading(depth+1) }}
    {% with schema=schema.kw_contains, skip_headers=False, depth=depth+1, skip_required=True %}
        {% include "content.md" %}
    {% endwith %}
{% endif %}

{% if schema.array_additional_items_def %}
    {{ "Additional items must be" | md_heading(depth+1) }}
    {% with schema=schema.array_additional_items_def, skip_headers=False, depth=depth+1, skip_required=True %}
        {% include "content.md" %}
    {% endwith %}
{% endif %}
