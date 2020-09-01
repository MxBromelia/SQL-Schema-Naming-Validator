import pytest
from . import adapter, validations
from validate_schema.mock_adapter import MockAdapter
from validate_schema.parse_configuration.build_configuration import ConfigurationBuilder

@pytest.fixture
def adapter_module():
    return adapter

@pytest.fixture
def validations_module():
    return validations

@pytest.fixture
def build_mock_conn():
    """ Mock Database schema Adapter Factory """
    def _build_mock_conn(tables_info, functions_info=None, procedures_info=None):
        return MockAdapter(tables_info, functions_info, procedures_info)
    return _build_mock_conn

@pytest.fixture
def build_configuration_builder():
    """ Configuration Builder Factory """
    def _build(
        adapter_module='integration_test.adapter', adapter_class='Adapter',
        adapter_params=None, adapter_named_params=None,
        validations_module='integration_test.validations',
        ignore_tables=None, export_format='CLI'):
        return ConfigurationBuilder(
            adapter_module=adapter_module,
            adapter_class=adapter_class,
            adapter_params=adapter_params or [],
            adapter_named_params=adapter_named_params or {},
            validations_module=validations_module,
            ignore_tables=ignore_tables or [],
            export_format=export_format
        )
    return _build
