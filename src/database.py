from re import sub
from mysql.connector import Error, connect
from mysql.connector.connection import MySQLConnection
from pandas.core.frame import DataFrame
from Config import Config


def _get_sql_field_value(arr: list) -> str:
    return arr[0].value


def _sql_fields(arr: list) -> str:
    fields = list(map(_get_sql_field_value, arr))
    fields_size = len(fields)

    for i in range(0, fields_size, 2):
        fields.insert(i+1, ",")
    
    return "".join(fields)


# Create all SQL values placeholders.
def _sql_values(values_len: int):
    return sub("%s", "%s,", "".join(["%s"]*values_len))[:-1]


# Build SQL string.
def sql_builder(database, table, fields, values_len) -> str:
    return f'INSERT INTO {database}.{table} ({_sql_fields(fields)}) VALUES ({_sql_values(values_len)});'


# Get all the values from data read.
def generate_values(data: DataFrame):
    return list(map(list, data.values))


# Create connection.
def create_connection(config: Config) -> MySQLConnection:
    try:
        return connect(host=config.host, port=config.port, database=config.name, user=config.user, password=config.password)
    except Exception as ex:
        print(ex)
        raise Exception("Unable to connect to database")
        

# Execute SQL.
def exec(connection: MySQLConnection, sql: str, data: DataFrame):
    try:
        # Get connection cursor.
        cursor = connection.cursor()

        # Execute the generated SQL per row of data.
        for value in generate_values(data):
            cursor.execute(sql, value)

        # Write changes to database.
        connection.commit()

        # Close connection.
        connection.close()
    
    # Catch all errors. Raise 'Unable to write to database' error for 'main.py' to handle.
    except Error as ex:
        print(ex)
        raise Exception("Unable to write to database.")