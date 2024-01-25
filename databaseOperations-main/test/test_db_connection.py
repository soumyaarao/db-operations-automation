import pytest
import psycopg2

from src.main import init_db


@pytest.fixture(scope='session')
def postgresql_url(request):
    config = request.config

    postgres_user = ""
    postgres_password = ""
    postgres_host = "localhost"
    postgres_port = "5432"
    postgres_database = "operations_db"
    return f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}"


@pytest.fixture
def database_connection(postgresql_url):
    print("postgresql_url", postgresql_url)
    connection = psycopg2.connect(postgresql_url)
    yield connection
    connection.close()

def test_postgresql_connection(database_connection):
    init_db('operations_db', '../database.sql')
    cursor = database_connection.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    assert result[0] == 1
    cursor.close()