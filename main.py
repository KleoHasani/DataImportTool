from click import command, argument, confirm, group, style
from getpass import getpass
from dit.globals import ascii_logo, ascii_done, DEFAULT_CONFIG_PATH
from dit.Config import Config
from dit.dataIO import read_data, read_mock
from dit.database import create_connection, sql_builder, exec


# Global config.
conf = Config(DEFAULT_CONFIG_PATH)


# Generate config file on user input.
@command(help="Set MySQL config and store to a config file.")
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


# Run, read mock and data and create sql and store to MYSQL database based on config.
@command(help="Import data from file to MySQL database.")
@argument("mock_file_path")
@argument("data_file_path")
def run(mock_file_path, data_file_path) -> None:
    # Load config.
    conf.load()

    # Create connection to database.
    db_conn = create_connection(conf)

    # Get table name and field columns from mock file.
    table, columns = read_mock(mock_file_path)

    # Ger data rows from data file.
    rows = read_data(data_file_path)

    # Generate SQL.
    sql = sql_builder(conf.get("database"), table, columns, len(columns))

    # Write to database.
    exec(db_conn, sql, rows)

    # Print DONE logo.
    print(f'{style(ascii_done, fg="green")}\n')


# CLI
@group(invoke_without_command=True, chain=True)
def cli():
    # Print app logo.
    print(f'{style(ascii_logo, fg="blue")}')
    pass

# Add commands to group.
cli.add_command(config, "config")
cli.add_command(run, "run")


# Only in dev.
if __name__ == "__main__":
    try:
        cli()
    except Exception as ex:
        print(f'\033[31m \n{ex} \033[0m \n')
