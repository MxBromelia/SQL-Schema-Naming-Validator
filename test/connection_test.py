import sqlite3
import pytest
from lib.connection import SQLiteConnection

@pytest.fixture
def sqlite_conn():
    """ A Connection with a Database containing two tables
        - products: Empty Table
        - contacts: Containting one element """
    with sqlite3.connect('temp/test.sqlite3') as conn:
        conn.execute('CREATE TABLE products(name TEXT)')

        conn.execute('CREATE TABLE contacts(first_name TEXT, last_name TEXT)')
        conn.execute("INSERT INTO contacts VALUES('Alan', 'Turing')")
        conn.commit()

    yield SQLiteConnection('temp/test.sqlite3')

    with sqlite3.connect('temp/test.sqlite3') as conn:
        conn.execute('DROP TABLE contacts')
        conn.execute('DROP TABLE products')
        conn.commit()

# SQLiteConnection
def test_execute_select_empty_table_return_empty_list(sqlite_conn):
    assert sqlite_conn.execute('SELECT * FROM PRODUCTS') == []

def test_execute_select_non_empty_table_return_its_data(sqlite_conn):
    assert sqlite_conn.execute('SELECT * FROM CONTACTS') == [{'first_name': 'Alan', 'last_name': 'Turing'}]

def test_execute_custom_select(sqlite_conn):
    assert sqlite_conn.execute('SELECT first_name FROM CONTACTS') == [{'first_name': 'Alan'}]


def test_tables_return_the_database_tables(sqlite_conn):
    assert sqlite_conn.tables() == ['CONTACTS', 'PRODUCTS']

def test_columns_return_the_tables_columns(sqlite_conn):
    assert sqlite_conn.columns('CONTACTS') == \
        [{'name': 'FIRST_NAME', 'type': 'TEXT'}, {'name': 'LAST_NAME', 'type': 'TEXT'}]