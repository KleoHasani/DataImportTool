from pandas import read_csv, read_excel;

def xlsx(path):
    df = read_excel(path)
    return df

def csv(path, separator = ","):
    df = read_csv(path, separator)
    return df

def mfile(path):
    file = open(path, "r")
    print(file.read())
    return file.read();