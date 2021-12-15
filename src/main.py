from click import command, argument, confirm, group, style
from getpass import getpass
from globals import ascii_logo, ascii_done, DEFAULT_CONFIG_PATH
from Config import Config
from dataIO import read_data, read_mock
from database import create_connection, sql_builder, exec


conf = Config(DEFAULT_CONFIG_PATH)


@command(help="Set MySQL config and store to file.")
def config() -> None:
    print("-- Enter Database configuration --")

    _host = input(f'{style(">", fg="green")} {style("Host: ", fg="yellow")}')
    _port = input(f'{style(">", fg="green")} {style("Port: ", fg="yellow")}')
    _database = input(f'{style(">", fg="green")} {style("Database: ", fg="yellow")}')
    _user = input(f'{style(">", fg="green")} {style("User: ", fg="yellow")}')
    _password = getpass(f'{style(">", fg="green")} {style("Password: ", fg="yellow")}')

    conf.set("host", _host)
    conf.set("port", _port)
    conf.set("database", _database)
    conf.set("user", _user)
    conf.set("password", _password)

    if confirm(f'Would you like to save this config? [{DEFAULT_CONFIG_PATH}]', default=True):
        conf.save()


@command(help="Import data from file to MySQL database.")
@argument("mock_file_path")
@argument("data_file_path")
def run(mock_file_path, data_file_path) -> None:
    conf.load()

    db_conn = create_connection(conf)

    table, columns = read_mock(mock_file_path)

    rows = read_data(data_file_path)

    sql = sql_builder(conf.get("database"), table, columns, len(columns))

    exec(db_conn, sql, rows)

    print(f'{style(ascii_done, fg="green")}\n')


# CLI
@group(invoke_without_command=True, chain=True)
def cli():
    print(f'{style(ascii_logo, fg="blue")}')
    pass

cli.add_command(config, "config")
cli.add_command(run, "run")


if __name__ == "__main__":
    try:
        cli()
    except Exception as ex:
        print(f'\033[31m \n{ex} \033[0m \n')
