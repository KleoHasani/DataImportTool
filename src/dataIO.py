from csv import reader
from json import load, dump
from os.path import exists
from re import split


# Read from CSV file if it exists.
def read_data(file_path: str) -> list:
    rows = list()

    try:
        # Get extention.
        ext = split("[(\/) | (\\) | (\.)]", file_path)[-1].lower()

        # Only CSV extentions are valid.
        if not ext == "csv":
            raise Exception("Invalid data file type.")
        
        # Check data file exists.
        if not exists(file_path):
            raise Exception("Data file does not exist.")
        
        # Read data file.
        with open(file_path, "r") as file:
            data = reader(file)
            
            # Skip/read header.
            next(data)

            # Read rows.
            for row in data:
                rows.append(row)

        return rows;

    # Catch all errors.
    except Exception as ex:
        print(ex)


# Read from dit.json config file if it exists.
def read_config(file_path: str) -> object:
    try:
        # Get config file name and extention.
        file = split("[(\/) | (\\)]", file_path)[-1].lower()

        # Ensure it's the proper config file.
        if not file == "dit.json":
            raise Exception("Invalid config file.")
        
        # Ensure config file exists.
        if not exists(file_path):
            raise Exception("Config file does not exist.")

        # Load config file.
        with open(file_path, "r") as file:
            return load(file)

    # Catch all errors.
    except Exception as ex:
        print(ex)
        raise ex


# Write config file to dit.json
def write_config(file_path: str, data: any) -> None:
    # Write data to file.
    with open(file_path, 'w') as file:
        dump(data, file)
    pass


# # Read from MOCK file if it exists.
def read_mock(file_path: str) -> tuple:
    try:
        # Get mock file extention.
        ext = split("[(\/) | (\\) | (\.)]", file_path)[-1].lower()

        # Ensure it's a mock file.
        if not ext == "mock":
            raise Exception("Invalid mock file type.")
        
        # Check file exists.
        if not exists(file_path):
            raise Exception("Mock file does not exist.")
        
        # Table name.
        table = None
        # Our database values.
        columns = list()
        
        # Read file.
        with open(file_path, "r") as file:
            # First line should be table name.
            table = file.readline()

            read = True
            while(read):
                # Read line and remove '\n' or '\r'
                line = file.readline().rstrip()

                if not line:
                    read = False
                    break

                # Our database columns are on left, data file columns are on right.
                sline = line.split("=")
                
                # Add to our collumns list for the fields generator.
                columns.append(sline[0])
        
        return (table, columns)

    # Catch all errors.
    except Exception as ex:
        print(ex)
        raise ex