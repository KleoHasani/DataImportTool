from pandas import read_csv, read_excel;
from src.Lexer import Lexer

def xlsx(path):
    data_frame = read_excel(path)
    return data_frame

def csv(path, separator = ","):
    data_frame = read_csv(path, delimiter=separator)
    return data_frame

def mfile(path):
    try:
        table_name = ""
        lex = Lexer()
        
        with open(path, "r") as file:
            table_name = file.readline().strip()

            can_read = True
            while(can_read):
                line = file.readline().strip()
                if not line:
                    can_read = False
                    break
                lex.consume(line)
        
        return (table_name, lex.getTokens())
        
    except Exception as ex:
        raise ex