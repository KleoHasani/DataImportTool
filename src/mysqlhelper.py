from os import environ
from dotenv import load_dotenv

load_dotenv(".env")

# ENV vars.
DB_HOST=environ.get("DB_HOST")
DB_USER=environ.get("DB_USER")
DB_PASSWORD=environ.get("DB_PASSWORD")
DB_NAME=environ.get("DB_NAME")

# Create new db connection and return connection.
def connect():
    return

# Execute SQL on the passed db connection.
def exec(conn):
    return

# Disconnect db from passed connection.
def disconnect(conn):
    return

