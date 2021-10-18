from pandas import read_csv;

def csv(path, separator = ","):
    df = read_csv(path, separator)
    return df

def xlsx(path):
    return