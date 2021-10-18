from userInput import cli
from dataReader import csv, xlsx
from mysqlHelper import connect, disconnect, exec 

def main():
    data = None
    cmd, cwp = cli()

    if cmd == "csv":
        data = csv(cwp)
        print(data)
        return

    if cmd == "xlsx":
        return

if __name__ == "__main__":
    main()