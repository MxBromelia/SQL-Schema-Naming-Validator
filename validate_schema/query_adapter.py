from typing import List, Dict, Optional
from .adapter import DBAdapter

class QueryAdapter:
    def __init__(self, adapter: DBAdapter):
        self._tables = adapter.tables()
        self._columns = adapter.columns()
        self._triggers = adapter.triggers()
        self._primary_keys = adapter.primary_keys()
        self._references = adapter.references()
        self._indexes = adapter.indexes()
        self._constraints = adapter.constraints()
        self._functions = adapter.functions()
        self._procedures = adapter.procedures()
        self._sequences = adapter.sequences()

    def tables(self) -> List[str]:
        return self._tables

    def columns(self, table_name: str) -> Dict[str, str]:
        return {
            column:ctype for (table, column, ctype)
            in self._columns
            if table == table_name
        }

    def triggers(self, table_name: str) -> Dict[str, str]:
        return {
            trigger:hook for (table, trigger, hook)
            in self._triggers
            if table == table_name
        }

    def primary_key(self, table_name: str, column_name: str) -> bool:
        return (table_name, column_name) in self._primary_keys

    def references(self, table_name: str, column_name: str) -> Optional[str]:
        return {
            (table, column): references for (table, column, references)
            in self._references
        }.get((table_name, column_name))

    def index(self, table_name: str, column_name: str) -> Optional[str]:
        for table, column, index in self._indexes:
            if table == table_name and column == column_name:
                return index
        return None

    def constraints(self, table_name: str, column_name: str) -> Dict[str, str]:
        return {
            constraint:ctype for (table, column, constraint, ctype)
            in self._constraints
            if table == table_name and column == column_name
        }

    def functions(self) -> List[str]:
        return self._functions

    def procedures(self) -> List[str]:
        return self._procedures

    def sequences(self) -> List[str]:
        return self._sequences
