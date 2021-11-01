from os import environ
from dotenv import load_dotenv
from mysql.connector import connect, Error

load_dotenv(".env")

DB_HOST=environ.get("DB_HOST")
DB_PORT=environ.get("DB_PORT")
DB_USER=environ.get("DB_USER")
DB_PASSWORD=environ.get("DB_PASSWORD")
DB_NAME=environ.get("DB_NAME")

def exec(self, data):
    try:
        with connect(
            host=self.DB_HOST,
            port=self.DB_PORT,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            database=self.DB_NAME
        ) as connection:
            print(connection)
    except Error as e:
        print(e)