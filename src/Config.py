from dataIO import read_config, write_config
from os import remove

class Config:
    def __init__(self, path: str) -> None:
        self.path = path
        self.config = {}
        pass


    def load(self) -> None:
        self.config = read_config(self.path)
        pass
    

    def set(self, item, value) -> None:
        self.config[item] = value
        pass

    
    def get(self, item: str) -> str:
        return self.config[item]


    def save(self) -> None:
        write_config(self.path, self.config)
        pass
    

    def delete(self) -> None:
        remove(self.path)
        pass