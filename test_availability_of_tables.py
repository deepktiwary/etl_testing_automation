from sql_query_running import *


def test_availability_of_tables():
    assert run_sql_query_for_validation('''
    select count(*) from sales
    ''')[0][0] >= 0


def test_availability_of_tables_sales_fact():
    assert run_sql_query_for_validation('''
    select count(*) from sales_fact
    ''')[0][0] >= 0