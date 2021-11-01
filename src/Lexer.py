TKN_COLM=0
TKN_MATC=1

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        return

class Lexer:
    def __init__(self):
        self.tokens=[]
        return

    def peak(self, exp, k):
        return exp[k]
    
    def consume(self, line):
        l = line.split("=")
        cline = l[0]
        sline  = l[1]

        column = Token(TKN_COLM, cline)
        matchers = []

        mline = sline.split("+")

        for match in mline:
            matchers.append(Token(TKN_MATC, match.strip()))
            
        self.tokens.append((column, matchers))
        return

    def getTokens(self):
        return self.tokens
