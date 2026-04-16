{# Display description #}
{% if schema.property_name %}
**Requirement:** {{ schema | schema_requirement_level }}
{% endif %}

{% if description %}
{{ description }}
{% endif %}
