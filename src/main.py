import cli;
import csvhelper as csv;

def main():
    cmd, cwp = cli.cli()

    if cmd == "csv":
        data = csv.read_csv(cwp)
        print(data)

    return

if __name__ == "__main__":
    main()