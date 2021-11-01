from src.helpers.cli import cli
from src.reader import csv, xlsx, mfile

def main():
    data = None
    cmd, cwp, m = cli()

    if cmd == "csv":
        data = csv(cwp)
        print(data)
        d1 = mfile(m)
        print(d1)
        return
      
    if cmd == "xlsx":
        data = xlsx(cwp)
        print(data)
        return

    return

if __name__ == "__main__":
    main()