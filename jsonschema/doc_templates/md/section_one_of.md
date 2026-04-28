Must be one of:
{% for enum_choice in schema.kw_enum.array_items %}
* {{ enum_choice.literal | python_to_json }}
{% endfor %}

{# If there are subschemas with details, show them compactly #}
{% if schema.kw_one_of or schema.kw_any_of %}
	{% for subschema in (schema.kw_one_of or schema.kw_any_of) %}
		{% if subschema.title or subschema.description %}
			- **{{ subschema.title or 'Option' }}**: {{ subschema.description or '' }}
		{% endif %}
	{% endfor %}
{% endif %}