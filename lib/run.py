from lib.validation import batch_validate_entities, ValidationConfig, \
    tables_to_validate, columns_to_validate
from lib.generate_schema import generate_schema
from lib.report import generate_report

def run(config: ValidationConfig):
    schema = generate_schema(config.connection)

    validation_tables = tables_to_validate(schema, config)
    validation_columns = columns_to_validate(schema, config)

    table_reports = {}
    table_vals = group_validations(
        batch_validate_entities(validation_tables, config.table_validations))
    for table, messages in table_vals.items():
        table_reports[table.name] = messages

    column_reports = {}
    column_vals = group_validations(
        batch_validate_entities(validation_columns, config.column_validations))
    for column, messages in column_vals.items():
        column_reports[f'{column.table.name}.{column.name}'] = messages

    # report = Report(table_reports=table_reports, column_reports=columns_reports)
    report = {'Tables': table_reports, 'Columns': column_reports}
    return generate_report(report)

def group_validations(validations):
    grouped = {}

    for validation in validations:
        if validation[0] not in grouped:
            grouped[validation[0]] = []

        grouped[validation[0]].append(validation[1])

    return grouped