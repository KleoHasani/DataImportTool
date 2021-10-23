import cli
import csvhelper as csv
import xlsxhelper as xlsx


def main():
    cmd, cwp = cli.cli()

    if cmd == "csv":
        data = csv.read_csv(cwp)
        print(data)
    elif cmd == "xlsx":
        data = xlsx.read(cwp)
        print(data)

    return


if __name__ == "__main__":
    main()
