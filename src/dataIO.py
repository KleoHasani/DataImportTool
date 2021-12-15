from csv import reader, DictReader
from os.path import exists, getsize
from re import split
from json import load, dump


# Read from CSV file if it exists.
def read_data(file_path: str) -> list:
    rows = list()

    try:
        ext = split("[(\/) | (\\) | (\.)]", file_path)[-1].lower()

        if not ext == "csv":
            raise Exception("Invalid data file type.")
        
        if not exists(file_path):
            raise Exception("Data file does not exist.")
        
        with open(file_path, "r") as file:
            data = reader(file)
            
            # Skip/read header.
            next(data)

            for row in data:
                rows.append(row)

        return rows;

    # Catch all errors.
    except Exception as ex:
        print(ex)


# Read from dit.json config file if it exists.
def read_config(file_path: str) -> object:
    try:
        file = split("[(\/) | (\\)]", file_path)[-1].lower()

        if not file == "dit.json":
            raise Exception("Invalid config file.")
        
        if not exists(file_path):
            raise Exception("Config file does not exist.")

        with open(file_path, "r") as file:
            return load(file)

    # Catch all errors.
    except Exception as ex:
        print(ex)
        raise ex


# Write config file to dit.json
def write_config(file_path: str, data: any) -> None:
    with open(file_path, 'w') as file:
        dump(data, file)


# # Read from MOCK file if it exists.
def read_mock(file_path: str) -> tuple:
    try:
        ext = split("[(\/) | (\\) | (\.)]", file_path)[-1].lower()

        if not ext == "mock":
            raise Exception("Invalid mock file type.")
        
        if not exists(file_path):
            raise Exception("Mock file does not exist.")
        
        table = None
        columns = list()
        
        with open(file_path, "r") as file:
            table = file.readline()

            read = True
            while(read):
                line = file.readline().rstrip()

                if not line:
                    read = False
                    break

                sline = line.split("=")

                columns.append(sline[0])
        
        return (table, columns)

    # Catch all errors.
    except Exception as ex:
        print(ex)
        raise ex