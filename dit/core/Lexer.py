from dit.core.Token import Token

TKN_COLM=0
TKN_MATC=1

# Lexer calss. Determine what a lexer can do. Hold on to tokens per lexer.
class Lexer:
    def __init__(self):
        # All tokens.
        self.tokens=[]
        return

    # Look ahead of the next character in a line.
    def peak(self, exp, k):
        return exp[k]
    
    # Tokenize the line.
    def consume(self, line):
        l = line.split("=")
        
        cline = l[0]
        sline  = l[1]

        column = Token(TKN_COLM, cline.strip())
        matchers = Token(TKN_MATC, sline.strip())

        self.tokens.append((column, matchers))
        return

    # Get all tokens.
    def getTokens(self):
        return self.tokens
