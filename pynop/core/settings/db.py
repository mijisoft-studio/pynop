import environ
import os

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Database
db_env = env('DB_ENV')

def get_db_env(key):
    new_key = db_env.upper() + '_' + key
    return env(new_key)

DB_CONFIG = {
    'env': db_env,
}
DB_CONFIG[db_env] = {
    'erp' : {
        'db_engine': 'DSN',
        'db_server': 'DSN=abc-erp',
        'db_name': '',
        'db_username': '',
        'db_password': ''
    },
    'staging': {
        'db_engine': get_db_env('STAGING_DB_ENGINE'),
        'db_server': get_db_env('STAGING_DB_SERVER'),
        'db_name': get_db_env('STAGING_DB_NAME'),
        'db_username': get_db_env('STAGING_DB_USERNAME'),
        'db_password': get_db_env('STAGING_DB_PASSWORD')
    },
    'nop': {
        'db_engine': get_db_env('NOP_DB_ENGINE'),
        'db_server': get_db_env('NOP_DB_SERVER'),
        'db_name': get_db_env('NOP_DB_NAME'),
        'db_username': get_db_env('NOP_DB_USERNAME'),
        'db_password': get_db_env('NOP_DB_PASSWORD')
    },
    'all': {
        'db_engine': 'MSSQL',
        'db_server': '192.168.253.223',
        'db_name': '',
        'db_username': 'sa',
        'db_password': ''
    }
}
