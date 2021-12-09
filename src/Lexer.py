from Token import Token, TKN_COLM, TKN_MATC

# Lexer calss. Determine what a lexer can do. Hold on to tokens per lexer.
class Lexer:
    def __init__(self) -> None:
        # All tokens.
        self.tokens=[]
        return
    
    # Tokenize the line.
    def consume(self, line) -> None:
        l = line.split("=")
        
        cline = l[0]
        sline  = l[1]

        column = Token(TKN_COLM, cline.strip())
        matchers = Token(TKN_MATC, sline.strip())

        self.tokens.append((column, matchers))
        return

    # Get all tokens.
    def getTokens(self) -> list:
        return self.tokens
