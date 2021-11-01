from src.helpers.cli import cli
from src.reader import csv, xlsx, mfile

def main():
    data = None
    cmd, cwp, m = cli()

    if cmd == "csv":
        data = csv(cwp)
        tokens = mfile(m)
        return
      
    if cmd == "xlsx":
        data = xlsx(cwp)
        print(data)
        return

if __name__ == "__main__":
    main()