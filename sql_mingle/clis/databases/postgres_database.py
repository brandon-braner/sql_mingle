from typing import List

from sql_mingle.clis.databases.abstract_database import AbstractDatabase
from dataclasses import dataclass

import psycopg
from psycopg.rows import dict_row

from sql_mingle.config import settings


class PostgresDatabase(AbstractDatabase):
    """
    Class for Postgres databases.
    """
    connection: psycopg.Connection

    def __init__(self):
        super().__init__()
        self.string_type = ['text', 'varchar', 'character varying', 'character']

    def connect(self):
        try:
            host = settings.postgres_settings['host']
            port = settings.postgres_settings['port']
            user = settings.postgres_settings['user']
            password = settings.postgres_settings['password']
            database = settings.postgres_settings['database']

            connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
            self.connection = psycopg.connect(connection_string, row_factory=dict_row)

        except (Exception, psycopg.DatabaseError) as error:
            print(error)  # Todo log error

    def get_schema(self, schema_name: str, table_name: str):
        """
        Get the column schema of a table.
        """
        query = f"""
                SELECT column_name, data_type, is_nullable, column_default,
                case
                    when character_maximum_length is not null
                        then character_maximum_length
                    else numeric_precision end as max_length
                FROM information_schema.columns
                WHERE table_name = %s
                AND table_schema = %s
            """

        cursor = self.connection.cursor()
        result = cursor.execute(query, (table_name, schema_name))
        return result.fetchall()
