from PySide6.QtWidgets import (
    QPushButton,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QFileDialog,
    QLineEdit,
)

from mutagen import (
    flac,
    mp3,
)

import os
from pathlib import Path


class Library(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.dir = ""
        self.song_paths = []

        choose_dir = QPushButton("Select Music Folder")
        choose_dir.clicked.connect(self.file_dialog)
        self.current_dir_text = QLineEdit()

        layout.addWidget(self.current_dir_text)
        layout.addWidget(choose_dir)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def file_dialog(self):
        directory = QFileDialog.getExistingDirectory(self, "Choose directory")
        if directory:
            self.current_dir_text.setText(f"{directory}")
            self.scandir(directory)
            print(self.song_paths)

    def scandir(self, path):
        current_dir = os.scandir(path)
        for i in current_dir:
            if i.is_dir():
                self.scandir(i.path)
            else:
                self.song_paths.append(f"{i.path}")
