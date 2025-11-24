from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
)

from PySide6.QtGui import (
    QPixmap,
)

import PySide6.QtCore


class Library(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.path = "/home/will/Music/Either_Or/cover.png"

    def update_library(self, track):
        albums_layout = QHBoxLayout()

        if len(track) > 0:
            cover = QLabel(self)
            path = track[0][8]
            pixmap = QPixmap(path)
            pixmap = pixmap.scaled(50, 50, PySide6.QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                   PySide6.QtCore.Qt.TransformationMode.SmoothTransformation)
            cover.setPixmap(pixmap)
            cover.setScaledContents(True)
            albums_layout.addWidget(cover)

        albums_layout.
        self.layout.addLayout(albums_layout)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

