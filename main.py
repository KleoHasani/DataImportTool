from src.cli import cli
from src.reader import csv, xlsx, mfile
from src.database import exec, sql_builder

def main():
    data = None
    cmd, cwp, m = cli()

    table_name, tokens = mfile(m)

    if cmd == "csv":
        data = csv(cwp)
      
    elif cmd == "xlsx":
        data = xlsx(cwp)
    
    else:
        print("Unsupported")
        return
    
    sql = sql_builder(table_name, tokens, data.shape)
    
    exec(sql, data)

    print("Done")

if __name__ == "__main__":
    main()