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
        main_layout = QVBoxLayout()

        if len(track) > 0:
            for i in range(len(track)):
                album_layout = QHBoxLayout()
                cover = QLabel(self)
                path = track[i][8]
                pixmap = QPixmap(path)
                pixmap = pixmap.scaled(50, 50, PySide6.QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                       PySide6.QtCore.Qt.TransformationMode.SmoothTransformation)
                cover.setPixmap(pixmap)
                cover.setGeometry(100, 100, 0, 0)
                album_layout.addWidget(cover)
                main_layout.addLayout(album_layout)

        self.layout.addLayout(main_layout)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

