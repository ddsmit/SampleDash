{% sql 'all', connection_string='sample.db' %}
SELECT
    *
FROM
    test
{% endsql %}

{% sql 'ids', connection_string='sample.db' %}
SELECT DISTINCT
    MACHINE_PERFORMED_PART_SEQUENCE
FROM
    test
{% endsql %}

{% sql 'get_ids', connection_string='sample.db' %}
SELECT
    *
FROM
    test
WHERE
    MACHINE_PERFORMED_PART_SEQUENCE in ({{ unit_list_query_string }})
{% endsql %}