from reader import conf_file
from Token import Token, TKN_MATC, TKN_COLM
from codecs import encode, decode


class Config:
    def __init__(self) -> None:
        self.config = [None] * 5
        pass


    def load_config(self, path: str) -> None:
        self.config = conf_file(path)
        pass
    

    def set_config(self, host, port, name, user, password) -> None:
        self.config[0] = [Token(TKN_COLM, "host"), Token(TKN_MATC, host)]
        self.config[1] = [Token(TKN_COLM, "port"), Token(TKN_MATC, port)]
        self.config[2] = [Token(TKN_COLM, "name"), Token(TKN_MATC, name)]
        self.config[3] = [Token(TKN_COLM, "user"), Token(TKN_MATC, user)]
        self.config[4] = [Token(TKN_COLM, "password"), Token(TKN_MATC, str(encode(password, "rot13")))]
        pass


    def to_string(self) -> str:
        return f"{self.config[0][0].value}={self.config[0][1].value}\n{self.config[1][0].value}={self.config[1][1].value}\n{self.config[2][0].value}={self.config[2][1].value}\n{self.config[3][0].value}={self.config[3][1].value}\n{self.config[4][0].value}={self.config[4][1].value}"


    @property
    def host(self) -> str:
        return self.config[0][1].value


    @property
    def port(self) -> str:
        return self.config[1][1].value


    @property
    def name(self) -> str:
        return self.config[2][1].value


    @property
    def user(self) -> str:
        return self.config[3][1].value


    @property
    def password(self) -> str:
        return str(decode(self.config[4][1].value, "rot13"))