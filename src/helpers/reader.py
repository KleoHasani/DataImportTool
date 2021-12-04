from pandas import read_csv, read_excel, DataFrame;
from core.Lexer import Lexer

# Read from xlsx file.
def xlsx(path) -> DataFrame:
    try:
        data_frame = read_excel(path)
        return data_frame
    
    # Catch all errors.
    except Exception:
        raise Exception("Unable to open file")

# Read from CSV file.
def csv(path, separator = ",") -> DataFrame:
    try:
        data_frame = read_csv(path, delimiter=separator)
        return data_frame

    # Catch all errors.
    except Exception:
        raise Exception("Unable to open file")

# Read from MOCK file.
def mfile(path) -> tuple:
    try:
        table_name = ""
        lex = Lexer()
        
        with open(path, "r") as file:
            # First line on MOCK file should be the database name.
            database_name = file.readline().strip()
            # Second line on MOCK file should be the database name.
            table_name = file.readline().strip()

            # Determine EOF, read until the end of file.
            can_read = True
            while(can_read):
                # read line and remove whitespaces.
                line = file.readline().strip()
                if not line:
                    can_read = False
                    break
                # Have the lexer consume this line to create tokens.
                lex.consume(line)

        # Return table name and tokens.
        return (database_name, table_name, lex.getTokens())
    # Catch all errors.
    except Exception:
        raise Exception("Unable to open file")