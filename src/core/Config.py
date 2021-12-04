from os.path import join, curdir, exists, abspath

class ConfigFile:
    def __init__(self, host, port, name, user, password) -> None:
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password
        return

class Config:
    def __init__(self) -> None:
        self.path = abspath(join(curdir, "dit.conf"))
        self.config = None
        self.exists = None


        if exists(self.path):
            self.exists = True
            try:
                with open(self.path, "r") as file:
                    data = file.read()
                    tokens = data.split("\n")
                    self.config = ConfigFile(tokens[0], tokens[1], tokens[2], tokens[3], tokens[4])
            except Exception:
                raise Exception("Unable to read config file.")

        else:
            self.exists = False
            try:
                with open(self.path, "w") as file:
                    file.close()
            except Exception:
                raise Exception("Unable to create config file.")

        return
    
    
    def setConfig(self, config: ConfigFile) -> None:
        self.config = config

    
    def saveConfig(self) -> None:
        try:
            with open(self.path, "w") as file:
                file.write(self.config.host + "\n" + self.config.port + "\n" + self.config.name + "\n" + self.config.user + "\n" + self.config.password)
                file.close()
        except Exception:
            raise Exception("Unable to save config.")
