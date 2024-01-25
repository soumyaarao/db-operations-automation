import psycopg2
import random
import string

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

class DatabaseOperations:
    def __init__(self, args):
        self.connection = psycopg2.connect(
            **args
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def fetch_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()