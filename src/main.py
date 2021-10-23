import cli
import csvhelper as csv
import xlsxhelper as xlsx
import mysqlhelper as db

def main():

    # data = None
    # cmd, cwp = cli()

    # if cmd == "csv":
    #     data = csv(cwp)
    #     print(data)
    #     return
      
    # if cmd == "xlsx":
    #     data = xlsx.read(cwp)
    #     print(data)
    #     return

    connection = db.connect()
    return

if __name__ == "__main__":
    main()