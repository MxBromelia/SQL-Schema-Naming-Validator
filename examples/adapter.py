from validate_schema.mock_adapter import MockAdapter

class Adapter(MockAdapter):
    def __init__(self):
        super().__init__({
            'metainfo': {
                'columns':{'alter_hash': 'text', 'comment': 'text'},
                'primary_key': 'id',
            },
            'tbl_user': {
                'columns': {'id': 'int', 'vc_username': 'varchar', 'vc_password': 'varchar'},
                'primary_key': 'id',
            },
            'tbl_product': {
                'columns': {'id': 'int', 'product_name': 'varchar', 'rl_price': 'real'},
                'primary_key': 'id',
            },
            'purchases': {
                'columns':{'buyer': 'int', 'product_id': 'int', 'nm_quantity': 'int'},
                'primary_key': 'buyer',
                'references': {'product_id': 'tbl_product'},
                'triggers': {'tg_new_product_history': 'after insert'}
            },
            'tbl_price_history': {
                'columns': {'product_id': 'int', 'history_price': 'real', 'dt_since': 'datetime'},
                'references': {'product_id': 'tbl_product'},
                'triggers': {'alter_product_price': 'after update'}
            },
        })
