import configparser


class Settings:
    def __init__(self):
        self.config = configparser.ConfigParser()

        self.config["Directory"] = {"Folder": ""}

    def get(self, section, setting):
        self.config.read("config.ini")
        value = self.config.get(section, setting)
        return value

    def set(self, section, setting, value):
        self.config.set(section, setting, value)

        with open("config.ini", "w") as configfile:
            self.config.write(configfile)

