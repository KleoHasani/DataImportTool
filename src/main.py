from click import command, argument

from re import split
from getpass import getpass
from os.path import exists, abspath

from Config import Config

from reader import csv, xlsx, mfile
from database import exec, create_connection, sql_builder


ascii_logo = '''
 ____________________________________________________________________
|                                                                    |
|    ___________              ___________            ___________     |
|   |  _______  \            |_____ _____|          |_____ _____|    |
|   | |        \ |                | |                    | |         |
|   | |        | |                | |                    | |         |
|   | |        | |                | |                    | |         |
|   | |        | |                | |                    | |         |
|   | |        | |                | |                    | |         |
|   | |        | |                | |                    | |         |
|   | |________/ |   _        ____| |____     _          | |         |
|   |___________/   |_|      |___________|   |_|         |_|         |
|                                                                    |
| Data Import Tool                                                   |
|____________________________________________________________________|
        https://github.com/csdcti/DataImportTool    By: CSDCTI Team.
'''

ascii_done = '''
_____________________
|                   |
|   * * Done * *    |
|___________________|
'''


@command(help="Config file path")
@argument("config_path")
def main(config_path) -> None:
    print(f'\033[36m{ascii_logo} \033[0m')

    # Global config.
    conf = Config(config_path)

    if not conf.exists():
        print("-- Enter Database configuration --")
        conf.host = input(f'\033[32m > \033[0m \033[33m Host    : \033[0m')
        conf.port = input(f'\033[32m > \033[0m \033[33m Port    : \033[0m')
        conf.name = input(f'\033[32m > \033[0m \033[33m Database: \033[0m')
        conf.user = input(f'\033[32m > \033[0m \033[33m User    : \033[0m')
        conf.password = getpass(f'\033[32m > \033[33m  Password: \033[0m')

    run = True

    while (run):
        print("-- Enter Files --")
        data_file_path = abspath(input(f'\033[32m > \033[0m \033[33m Data file path: \033[0m'))
        mock_file_path = abspath(input(f'\033[32m > \033[0m \033[33m Mock file path: \033[0m'))

        try:
            # Check files exist
            if not exists(data_file_path):
                raise Exception("Data file does not exist")
            
            if not exists(mock_file_path):
                raise Exception("Mock file does not exist")

            ext = split("[(\/) | (\\) | (\.)]", data_file_path)[-1].lower()

            # Read mock file and determine database and table name and provide mock data tokens.
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
            sql = sql_builder(conf.name, table_name, tokens, data.shape[1])
            
            # Execute SQL and save.
            conn = create_connection(conf)

            # Create connection to database.
            exec(conn, sql, data)

            print(f'\033[0m \033[32m {ascii_done} \033[0m\n')
            
        except Exception as ex:
            print(f'\033[31m \n{ex} \033[0m \n')
        
        again = input(f'\033[32m > \033[0m \033[33m [Q/q] \033[0m to quit. \033[33m [Enter] \033[0m to run again: ')

        if again == "Q" or again == "q":
            run = False
            exit(0)


if __name__ == "__main__":
    main()