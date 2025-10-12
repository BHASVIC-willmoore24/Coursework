import configparser


class Settings:
    def __init__(self):
        self.config = configparser.ConfigParser()


    def get(self, section, setting):
        self.config.read("config.ini")
        value = self.config.get(section, setting)
        return value

    def set(self, section, setting, value):
        self.config.set(section, setting, value)

    def add(self, section, setting, value):
        self.config[section] = {setting: value}

