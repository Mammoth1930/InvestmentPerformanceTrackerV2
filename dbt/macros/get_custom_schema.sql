/*
    This macro overrides the default schema name generation in dbt.
    It allows for a custom schema name to be provided, or default to the target schema defined in profiles.yml.
*/
{% macro generate_schema_name(custom_schema_name, node) -%}

    -- Get default schema from profiles.yml
    {%- set default_schema = target.schema -%}
    {%- if custom_schema_name is none -%}

        {{ default_schema }}

    {%- else -%}

        {{ custom_schema_name | trim }}

    {%- endif -%}

{%- endmacro %}