import typer
from re import split
from os.path import exists, abspath
from src.reader import csv, xlsx, mfile
from src.database import exec, sql_builder

def main(data_file_path: str, mock_file_path: str):
    try:
        # Check files exist
        if not exists(data_file_path):
            raise Exception("Data file does not exist")
        
        if not exists(mock_file_path):
            raise Exception("Mock file does not exist")

        # Get absolute path for files.
        data_file_path = abspath(data_file_path)          
        mock_file_path = abspath(mock_file_path)

        ext = split("[(\/) | (\\) | (\.)]", data_file_path)[-1].lower()

        # Read mock file and determine database table name, and provide mock data tokens.
        table_name, tokens = mfile(mock_file_path)

        # Data variable.
        data = None

        # Check which reader to use.
        if ext == "csv":
            data = csv(data_file_path)
        
        if ext == "xlsx":
            data = xlsx(data_file_path)

        #Build SQL statement based on table name, tokens and data size.
        sql = sql_builder(table_name, tokens, data.shape)
        
        # Execute SQL and save.
        exec(sql, data)

        print("Done")
        
    except Exception as ex:
        print(ex)
    
    # Exit
    typer.Exit()
    return


if __name__ == "__main__":
    typer.run(main)