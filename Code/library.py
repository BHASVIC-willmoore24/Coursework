from PySide6.QtWidgets import (
    QPushButton,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
)

from PySide6.QtGui import (
    QPixmap,
)


class Library(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tracks = []

    def update_library(self, track_list):
        self.tracks = track_list

    def update_library(self, tracks):

        layout = QVBoxLayout()
        album_layout = QHBoxLayout()
        play_button = QPushButton("test widget")
        album_layout.addWidget(play_button)

        cover = QLabel(self)
        cover_path = "C:/Users/will.moore24/Music/Either_Or/cover.png"
        pixmap = QPixmap(cover_path)
        cover.setPixmap(pixmap)
        album_layout.addWidget(cover)

        layout.addLayout(album_layout)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


""" 
        for i in range(len(tracks)):
            cover = QLabel(self)
            cover_path = tracks[i][8]
            pixmap = QPixmap(cover_path)
            cover.setPixmap(pixmap)
            album_layout.addWidget(cover)
"""