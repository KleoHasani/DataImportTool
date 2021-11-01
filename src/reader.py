from pandas import read_csv, read_excel;
from src.Lexer import Lexer

def xlsx(path):
    df = read_excel(path)
    return df

def csv(path, separator = ","):
    df = read_csv(path, separator)
    return df

def mfile(path):
    try:
        lex = Lexer()
        
        with open(path, "r") as file:
            line = file.readline()
            lex.consume(line)
        
        return lex
    except Exception as ex:
        raise ex;