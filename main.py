from src.cli import cli
from src.reader import csv, xlsx, mfile
from src.database import exec, sql_builder

def main():
    # Data from file variable.
    data = None

    # CLI tupple returns.
    # cmd = command supplied by user.
    # cwp = current data file path.
    # mck = current mock file path.
    cmd, cwp, mck = cli()

    # Read mock file and determine database table name, and provide mock data tokens.
    table_name, tokens = mfile(mck)        
    
    # Determine which reader to use.
    if cmd == "xlsx":
        data = xlsx(cwp)
    else:
        data = csv(cwp)
    
    # Build SQL statement based on table name, tokens and data size.
    sql = sql_builder(table_name, tokens, data.shape)
    
    # Execute SQL and save.
    exec(sql, data)

    print("Done")
    exit(0)

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(ex)
        exit(1)