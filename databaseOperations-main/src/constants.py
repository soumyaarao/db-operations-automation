# DB_HOST = "localhost"
# DB_PORT = "5432"
# DB_NAME = "operations_db"
# DB_USER = "soumyarao"
# DB_PASSWORD = "mypassword"
#
#
# # constants.py
import configparser
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

config_file_path = os.path.join(script_dir, 'config.ini')

print(f"Config file path: {config_file_path}")

# Read the configuration file
config = configparser.ConfigParser()
config.read(config_file_path)

DB_HOST = config.get('database', 'host')
DB_PORT = config.get('database', 'port')
DB_NAME = config.get('database', 'name')
DB_USER = config.get('database', 'user')
DB_PASSWORD = config.get('database', 'password')
