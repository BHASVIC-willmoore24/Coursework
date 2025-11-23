from PySide6.QtWidgets import (
    QPushButton,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
)

from PySide6.QtCore import QTimer

from PySide6.QtGui import (
    QPixmap,
)

from stored_music import StoredMusic


class Library(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.path = "/home/will/Music/Either_Or/cover.png"

        self.tracks = []

        reload_button = QPushButton("Reload Library")
        reload_button.setCheckable(True)
        reload_button.clicked.connect(self.clicked_button)

        self.layout.addWidget(reload_button)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def clicked_button(self):
        print(self.tracks)
        self.update_library(self.tracks)

    def set_tracks(self, pTrack):
        self.tracks = pTrack
        print(self.tracks)

    def update_library(self, pTrack):
        albums_layout = QHBoxLayout()

        if len(pTrack) > 0:
            cover = QLabel(self)
            path = pTrack[0][8]
            pixmap = QPixmap(path)
            cover.setPixmap(pixmap)
            cover.resize(100, 100)
            albums_layout.addWidget(cover)

        self.layout.addLayout(albums_layout)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

