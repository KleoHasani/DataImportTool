from click import command, argument, confirm, group

from re import split
from getpass import getpass

from Config import Config
from globals import ascii_logo, ascii_done, DEFAULT_CONFIG_PATH

from reader import csv, xlsx, mfile
from database import exec, create_connection, sql_builder


conf = Config()

@command(help="Set MySQL config and store to file.")
def config() -> None:
    print("-- Enter Database configuration --")
    _host = input(f'\033[32m > \033[0m \033[33m Host    : \033[0m')
    _port = input(f'\033[32m > \033[0m \033[33m Port    : \033[0m')
    _name = input(f'\033[32m > \033[0m \033[33m Database: \033[0m')
    _user = input(f'\033[32m > \033[0m \033[33m User    : \033[0m')
    _password = getpass(f'\033[32m > \033[33m  Password: \033[0m')

    conf.set_config(_host, _port, _name, _user, _password)

    save = confirm(f'Would you like to save this config? [{DEFAULT_CONFIG_PATH}]', default=True)

    if save:
        with open(DEFAULT_CONFIG_PATH, "w") as file:
            file.write(conf.to_string())


@command(help="Import data from file to MySQL database.")
@argument("mock_file_path")
@argument("data_file_path")
def run(mock_file_path, data_file_path) -> None:
    conf.load_config(DEFAULT_CONFIG_PATH)

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


# CLI
@group(invoke_without_command=True, chain=True)
def cli():
    print(f'\033[36m{ascii_logo} \033[0m')
    pass

cli.add_command(config, "config")
cli.add_command(run, "run")


if __name__ == "__main__":
    try:
        cli()
    except Exception as ex:
        print(f'\033[31m \n{ex} \033[0m \n')
