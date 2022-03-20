import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Database settings
    postgres_settings: dict = {
        'host': os.environ.get('POSTGRES_HOST', 'localhost'),
        'port': os.environ.get('POSTGRES_PORT', 5432),
        'user': os.environ.get('POSTGRES_USER', 'postgres'),
        'password': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'database': os.environ.get('POSTGRES_DB', 'postgres'),
    }

    bigquery_settings: dict = {
        'json_key_file_path': os.environ.get('BIGQUERY_JSON_KEY_FILE_PATH', None)
    }


settings = Settings()
