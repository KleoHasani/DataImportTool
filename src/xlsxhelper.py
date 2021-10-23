from pandas import read_excel

def read(path):
    df = read_excel(path)
    return df
