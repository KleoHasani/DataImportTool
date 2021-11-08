from os import environ
from dotenv import load_dotenv
from mysql.connector import connect, Error

load_dotenv(".env")

# ENV defined variables to connect to MYSQL.
DB_HOST=environ.get("DB_HOST")
DB_PORT=environ.get("DB_PORT")
DB_USER=environ.get("DB_USER")
DB_PASSWORD=environ.get("DB_PASSWORD")
DB_NAME=environ.get("DB_NAME")

# Get all the values from data read.
def gen_values(data):
    values = []

    for i in range(0, data.shape[0]):
        values.append(list(data.iloc[i]))

    return values


# Build SQL statement.
def sql_builder(table, tokens, shape):
    # Current SQL.
    sql = None

    # Length of tokens.
    tokens_len = len(tokens)

    # Lenght of data. Rows and Columns
    shape_len = shape

    # Basic 'INSERT INTO' SQL statement.
    sql_start = "INSERT INTO " + DB_NAME + "." + table
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

def exec(sql, data):
    try:
        # Create connection to database.
        cnx = connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME)

        # Get connection cursor.
        cursor = cnx.cursor()

        # Execute the generated SQL per row of data.
        for value in gen_values(data):
            cursor.execute(sql, value)

        # Write changes to database.
        cnx.commit()

        # Close connection.
        cnx.close()
    
    # Catch all errors. Raise 'Unable to write to database' error for 'main.py' to handle.
    except Error as ex:
        raise Exception("Unable to write to database.")