from os.path import abspath, exists

from reader import conf_file


class Config:
    def __init__(self, path: str) -> None:
        self.config = []

        path = abspath(path)

        if exists(path):
            self.config = conf_file(path)

    
    def exists(self) -> bool:
        if len(self.config) > 0:
            return True
        return False

    @property
    def host(self):
        return self.config[0][1].value

    @property
    def port(self):
        return self.config[1][1].value

    @property
    def name(self):
        return self.config[2][1].value
    
    @property
    def user(self):
        return self.config[3][1].value

    @property
    def password(self):
        return self.config[4][1].value