import configparser

from PySide6.QtWidgets import (
    QPushButton,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QFileDialog,
    QLineEdit,
)

import os

class Settings(QMainWindow):
    def __init__(self, library, stored_music):
        super().__init__()
        layout = QVBoxLayout()
        self.library = library
        self.stored_music = stored_music

        # config file .ini
        self.config = configparser.ConfigParser()
        self.config["Directory"] = {"Folder": ""}

        self.dir = self.get_conf("Directory", "folder")

        choose_dir = QPushButton("Select Music Folder")
        choose_dir.clicked.connect(self.file_dialog)
        self.current_dir_text = QLineEdit()

        if self.dir != "":
            self.current_dir_text.setText(f"{self.dir}")
            self.scandir(self.dir)
            # calls update_library method at the start of the program
            tracks_full = stored_music.get_metadata()
            self.library.update_library(tracks_full)

        layout.addWidget(self.current_dir_text)
        layout.addWidget(choose_dir)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # opens up a file dialog window to select directory
    def file_dialog(self):
        directory = QFileDialog.getExistingDirectory(self, "Choose directory")
        if directory:
            self.current_dir_text.setText(f"{directory}")
            self.set_conf("Directory", "folder", directory)
            self.stored_music.clear_song_paths()
            self.scandir(directory)
            # calls update_library method whenever library is updated
            tracks_full = self.stored_music.get_metadata()
            self.library.update_library(tracks_full)

    # recursive function scans through entire directory
    def scandir(self, path):
        current_dir = os.scandir(path)
        for i in current_dir:
            if i.is_dir():
                self.scandir(i.path)
            else:
                self.stored_music.append_song_paths(i.path)

    # methods for the config file
    def get_conf(self, section, setting):
        self.config.read("config.ini")
        value = self.config.get(section, setting)
        return value

    def set_conf(self, section, setting, value):
        self.config.set(section, setting, value)

        with open("config.ini", "w") as configfile:
            self.config.write(configfile)
