class Config:
    def __init__(self, host = None, port= None, name= None, user= None, password= None) -> None:
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password
        return
    
    def exists(self) -> bool:
        if self.host and self.port and self.name and self.user and self.password:
            return True
        return False
