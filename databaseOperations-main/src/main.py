import subprocess
import sys
import shutil
import platform
import os


def is_postgresql_installed():
    try:
        # Check if 'psql' executable exists
        shutil.which('psql', mode=os.X_OK)
        return True
    except shutil.Error:
        return False


def install_postgresql():
    os_name = platform.system().lower()

    try:
        if os_name == 'linux':
            subprocess.run(['sudo', 'apt', 'install', 'postgresql'], check=True)
            subprocess.run(['systemctl', 'start', 'postgresql.service'])
        elif os_name == 'darwin':
            subprocess.run(['brew', 'install', 'postgresql'], check=True)
            subprocess.run(['brew', 'services', 'start', 'postgresql'])
        else:
            print(f"Unsupported operating system: {os_name}. Please install PostgreSQL manually.")
            sys.exit(1)

        print("PostgreSQL installed successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install PostgreSQL on {os_name}. Please install it manually.")
        sys.exit(1)

def load_database_script(script_path):
    try:
        subprocess.run([
            'psql',
            'postgres',
            '-f', script_path,
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error loading script: {e}")
        raise

def setupDB():
    install_postgresql()

def is_db_created(db_name):
    try:
        # Construct the psql command to list all databases
        command = [
            'psql',
            'postgres',
            '-c', '\\l'
        ]

        output = subprocess.check_output(command, text=True, stderr=subprocess.PIPE)
        return db_name in output

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
def init_db(db_name, script_path):
    setupDB()
    if not is_db_created(db_name):
        load_database_script(script_path)

    print("Database loaded!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_db('operations_db', '../database.sql')

