from sql_mingle.clis.databases.postgres_database import PostgresDatabase


def test_postgres_connection():
    """Test connecting to a Postgres database."""
    db = PostgresDatabase()
    db.connect()
    assert str(type(db.connection)) == "<class 'psycopg.Connection'>"


def test_getting_table_schema():
    """Ensure we can get the table schema."""
    db = PostgresDatabase()
    db.connect()
    result = db.get_schema('public', 'test_table')
    assert len(result) == 5


def test_add_internal_column_type():
    """Ensure we can add an internal column type."""
    db = PostgresDatabase()
    db.connect()
    result = db.get_schema('public', 'test_table')
    column_type = db.add_internal_column_type(schema_column_type=result[0]['data_type'])
    assert column_type == 'string_type'