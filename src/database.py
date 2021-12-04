from mysql.connector import Error, connect

from .Config import Config

# Get all the values from data read.
def gen_values(data):
    values = []

    for i in range(0, data.shape[0]):
        values.append(list(data.iloc[i]))

    return values


# Build SQL statement.
def sql_builder(database, table, tokens, shape):
    # Current SQL.
    sql = None

    # Length of tokens.
    tokens_len = len(tokens)

    # Lenght of data. Rows and Columns
    shape_len = shape

    # Basic 'INSERT INTO' SQL statement.
    sql_start = "INSERT INTO " + database + "." + table
    sql_fields = " ("
    sql_values = " VALUES ("

    # Build filed names.
    for i in range (0, tokens_len):
        # Append field.
        sql_fields = sql_fields + tokens[i][0].value

        # Append separator.
        if (i < tokens_len - 1):
            sql_fields = sql_fields + ","

    # Append close fields tag.
    sql_fields = sql_fields + ")"
    
    # Append placeholders for values.
    for j in range (0, shape_len[1]):
        sql_values = sql_values + "%s"
        
        # Append separator.
        if (j < shape_len[1] - 1):
            sql_values = sql_values + ","

    # Append close values tag.
    sql_values = sql_values + ");"

    # Build SQL statement.
    sql = sql_start + sql_fields + sql_values

    return sql


def create_connection(config: Config):
    try:
        return connect(host=config.host, port=config.port, database=config.name, user=config.user, password=config.password)
    except Exception:
         raise Exception("Unable to connect to database")
        

def exec(connection, sql, data):
    try:
        # Get connection cursor.
        cursor = connection.cursor()

        # Execute the generated SQL per row of data.
        for value in gen_values(data):
            cursor.execute(sql, value)

        # Write changes to database.
        connection.commit()

        # Close connection.
        connection.close()
    
    # Catch all errors. Raise 'Unable to write to database' error for 'main.py' to handle.
    except Error as ex:
        raise Exception("Unable to write to database.")