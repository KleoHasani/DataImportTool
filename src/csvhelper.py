from pandas import read_csv;

def read(path, separator = ","):
    df = read_csv(path, separator)
    return df