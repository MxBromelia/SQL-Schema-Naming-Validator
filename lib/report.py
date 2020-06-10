""" Generate the Report Output to the schema validation

Report Example:

REPORT
=================================================

Tables:
=================================================
 + table_one
   + message one
   + message two
---------------------------------------

Columns:
=================================================
 + table_one.column_one
   + message one
---------------------------------------
 + table_one.column_two
   + message one
---------------------------------------
"""
from typing import List, Dict

def entity_report(entity_name: str, messages: List[str]) -> List[str]:
    """ Serializes the messages of a given entity to the Report

    It generates a list that translates as:

     + entity
       + message one
       + message two"""
    return [f' + {entity_name}'] + [f'   + {message}' for message in messages]

def entities_report(entity_group: str, entities: Dict[str, List[str]]) -> List[str]:
    """ Serializes the messages to a group of entities to the Report """
    output = [f'{entity_group}:', '=' * 50]
    for entity, messages in entities.items():
        output += entity_report(entity, messages)
        output.append('-' * 40)
    return output

# entities_report: { 'entity_group': { 'entity': ['message'] } }
def generate_report(report_hash: Dict[str, Dict[str, List[str]]]) -> List[str]:
    """ Receives an Dict containing the Report info, divided in:
        key -> The Entity Group (Ex.: Table, Columns)
        value -> A Dict containing the Entities and its messages
            key -> The Entity unique name (Ex.: table_one, table_one.column_one)
            value -> A list of Strings containing the Validations Mistakes in the Report"""
    output = ['REPORT', '=' * 50]

    for entity_group, entities in report_hash.items():
        output += entities_report(entity_group, entities)
    return output