""" Validations """
from typing import Callable, List, Tuple, Union
from .schema import Table, Schema, Column
from .connection import DBConnection

def validate_entity(entity: Union[Table, Column], validations: List[Callable]) -> List[str]:
    """ Run a list of validations for an entity """
    if entity is None:
        raise TypeError
    if len(validations) == 0:
        raise ValueError

    raw_messages = [val(entity) for val in validations]
    return [message for message in raw_messages if message is not None]

def batch_validate_entities(entities: List, validations: List[Callable]) -> List:
    """ Run a list of validations for a list of entities """
    val_res: List[Tuple] = []

    for entity in entities:
        val_res += [(entity, message) for message in validate_entity(entity, validations)]

    return val_res

class ValidationConfig:
    """ Stores and configuration options for running the validations """
    def __init__(self, table_validations: List[Callable], column_validations: List[Callable],
                 connection: DBConnection, ignore_tables: List[str] = None):
        self.ignore_tables: List[str] = [] if ignore_tables is None else ignore_tables
        self.table_validations: List[Callable] = table_validations
        self.column_validations: List[Callable] = column_validations
        self.connection: DBConnection = connection

def tables_to_validate(schema: Schema, config: ValidationConfig):
    """ Filter Entity Tables to ignore the ones specified in configuration """
    if schema is None or config is None:
        raise TypeError
    return [table for table in schema.tables if table.name not in config.ignore_tables]

def columns_to_validate(schema: Schema, config: ValidationConfig):
    if schema is None or config is None:
        raise TypeError
    return [column for column in schema.columns() if column.table is not None and column.table.name not in config.ignore_tables]
