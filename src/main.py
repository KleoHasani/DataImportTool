from helpers.cli import cli
from reader import csv, xlsx
from database import exec

def main():
    data = None
    cmd, cwp = cli()

    if cmd == "csv":
        data = csv(cwp)
        print(data)
        return
      
    if cmd == "xlsx":
        data = xlsx(cwp)
        print(data)
        return

    return

if __name__ == "__main__":
    main()