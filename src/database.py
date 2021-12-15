from re import sub
from mysql.connector import Error, connect
from mysql.connector.connection import MySQLConnection
from Config import Config


def _sql_fields(arr: list) -> str:
    fields_size = len(arr)

    for i in range(0, fields_size, 2):
        arr.insert(i+1, ",")
    
    return "".join(arr)


# Build SQL string.
def sql_builder(database, table, fields, values_len) -> str:
    return f'INSERT INTO {database}.{table} ({_sql_fields(fields)}) VALUES ({sub("%s", "%s,", "".join(["%s"]*values_len))[:-1]});'


# Create connection.
def create_connection(config: Config) -> MySQLConnection:
    try:
        return connect(host=config.get("host"), port=config.get("port"), database=config.get("database"), user=config.get("user"), password=config.get("password"))
    except Exception as ex:
        print(ex)
        raise Exception("Unable to connect to database")
        

# Execute SQL.
def exec(connection: MySQLConnection, sql: str, data: list):
    try:
        # Get connection cursor.
        cursor = connection.cursor()

        cursor.executemany(sql, data)

        # Write changes to database.
        connection.commit()

        # Close connection.
        connection.close()
    
    # Catch all errors. Raise 'Unable to write to database' error for 'main.py' to handle.
    except Error as ex:
        print(ex)
        raise Exception("Unable to write to database.")