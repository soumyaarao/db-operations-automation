from unittest import TestCase

from src.db_operations import DatabaseOperations, generate_random_string
from src.constants import DB_HOST, DB_PORT, DB_NAME
from src.main import init_db


class TestDataBaseOperations(TestCase):
    def setUp(self):
        init_db('operations_db', '../database.sql')
        connection_args = {
            "host" : DB_HOST,
            "port" : DB_PORT,
            "database" : DB_NAME,
        }
        self.db_connection = DatabaseOperations(connection_args)


    def test_dml_operations(self):
        name = generate_random_string()
        email = generate_random_string() + '@example.com'

        # DML Operation
        insert_query = f"INSERT INTO user_details (name, email) VALUES ('{name}', '{email}')"
        self.db_connection.execute_query(insert_query)

        # Validation
        select_query = f"SELECT * FROM user_details WHERE name = '{name}'"
        result = self.db_connection.fetch_data(select_query)
        assert len(result) == 1
        assert result[0][1] == name
        assert result[0][2] == email


    def test_ddl_operations(self):
        create_table_query = """
           CREATE TABLE IF NOT EXISTS product (
               id SERIAL PRIMARY KEY,
               name VARCHAR(255) NOT NULL,
               price DECIMAL(10, 2) NOT NULL
           )
           """
        self.db_connection.execute_query(create_table_query)

        # Validation
        table_exists_query = "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'product')"
        result = self.db_connection.fetch_data(table_exists_query)
        assert result[0][0] is True