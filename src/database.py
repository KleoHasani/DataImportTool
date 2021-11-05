from os import environ
from dotenv import load_dotenv
from mysql.connector import connect, Error

load_dotenv(".env")

DB_HOST=environ.get("DB_HOST")
DB_PORT=environ.get("DB_PORT")
DB_USER=environ.get("DB_USER")
DB_PASSWORD=environ.get("DB_PASSWORD")
DB_NAME=environ.get("DB_NAME")

def format_sql_string(text):
    return "'"+text+"'"


def gen_values(data):
    values = []

    for i in range(0, data.shape[0]):
        values.append(list(data.iloc[i]))

    return values


def sql_builder(table, tokens, shape):
    sql = None

    tokens_len = len(tokens)

    shape_len = shape

    sql_start = "INSERT INTO " + DB_NAME + "." + table
    sql_fields = " ("
    sql_values = " VALUES ("

    for i in range (0, tokens_len):
        sql_fields = sql_fields + tokens[i][0].value

        if (i < tokens_len - 1):
            sql_fields = sql_fields + ","

    sql_fields = sql_fields + ")"
        
    for j in range (0, shape_len[1]):
        sql_values = sql_values + "%s"
        
        if (j < shape_len[1] - 1):
            sql_values = sql_values + ","

    sql_values = sql_values + ");"

    sql = sql_start + sql_fields + sql_values

    return sql

def exec(sql, data):
    try:
        cnx = connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME)

        cursor = cnx.cursor()

        for value in gen_values(data):
            cursor.execute(sql, value)

        cnx.commit()
        cnx.close()
    except Error as e:
        print(e)