# pylint: disable = missing-module-docstring
# pylint: disable = missing-function-docstring

from sql_judge.export.cli import export_cli
from sql_judge.export.cli import _entity_report
from sql_judge.validate import Fail

def test_generate_entity_report_one_message():
    assert _entity_report('table_one', ['message one']) == \
        [' + table_one', '   + message one']

def test_generate_entity_report_two_messages():
    assert _entity_report('table_one.column_one', ['message one', 'message two']) == \
        [' + table_one.column_one', '   + message one', '   + message two']

def test_generate_report_one_entity():
    report = [Fail('Tables', 'table_one', 'message one')]

    assert export_cli(report) == [
        'REPORT', '=' * 50, 'Tables:', '=' * 50,
        ' + table_one', '   + message one', '-' * 40
    ]

def test_generate_report_two_entities():
    report = [
        Fail('Columns', 'table_one.column_one', 'message one'),
        Fail('Columns', 'table_one.column_two', 'message two')
    ]

    assert export_cli(report) == [
        'REPORT', '=' * 50, 'Columns:', '=' * 50,
        ' + table_one.column_one', '   + message one', '-' * 40,
        ' + table_one.column_two', '   + message two', '-' * 40
    ]

def test_generate_report_two_distinct_entities():
    report = [
        Fail('Tables', 'table_one', 'message one'),
        Fail('Columns', 'table_one.column_one', 'message one')
    ]

    assert export_cli(report) == [
        'REPORT', '=' * 50,
        'Tables:', '=' * 50,
        ' + table_one', '   + message one', '-' * 40,
        'Columns:', '=' * 50,
        ' + table_one.column_one', '   + message one', '-' * 40
    ]
