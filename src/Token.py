TKN_COLM=0
TKN_MATC=1

# Token class. Determine how a token will look.
class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value
        return