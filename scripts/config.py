import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE not in sys.path:
    sys.path.insert(0, BASE)

from pipeline.config import load_config


config = load_config()

DB_HOST = config.postgres_host
DB_PORT = str(config.postgres_port)
DB_NAME = config.postgres_db
DB_USER = config.postgres_user
DB_PASSWORD = config.postgres_password
