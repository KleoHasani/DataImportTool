import click
from re import split
from os.path import exists, abspath
from dit.core.reader import csv, xlsx, mfile
from dit.core.database import exec, sql_builder


@click.command()
@click.argument('data_file_path')
@click.argument('mock_file_path')
def main(data_file_path, mock_file_path):
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
        
        elif ext == "xlsx":
            data = xlsx(data_file_path)
        
        else:
            raise Exception("Invalid file type.")


        #Build SQL statement based on table name, tokens and data size.
        sql = sql_builder(table_name, tokens, data.shape)
        
        # Execute SQL and save.
        exec(sql, data)

        print("Done")
        
    except Exception as ex:
        print(ex)
    
    # Exit
    exit(0)
    return


if __name__ == "__main__":
    main()