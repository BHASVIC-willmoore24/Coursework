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

    # using a method to update library display so this can be called in other classes
    def update_library(self, track):
        main_layout = QVBoxLayout()

        if len(track) > 0:
            for i in range(len(track)):
                album_layout = QHBoxLayout()
                info_layout = QVBoxLayout()

                cover = QLabel(self)
                path = track[i][8]
                pixmap = QPixmap(path)
                pixmap = pixmap.scaled(50, 50, PySide6.QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                                       PySide6.QtCore.Qt.TransformationMode.SmoothTransformation)
                cover.setPixmap(pixmap)
                cover.setGeometry(100, 100, 0, 0)
                album_layout.addWidget(cover)

                title = QLabel(self)
                title.setText(" ".join(track[i][3]))
                info_layout.addWidget(title)

                album = QLabel(self)
                album.setText(" ".join(track[i][2]))
                info_layout.addWidget(album)

                artist = QLabel(self)
                artist.setText(" ".join(track[i][1]))
                info_layout.addWidget(artist)

                album_layout.addLayout(info_layout)
                main_layout.addLayout(album_layout)

        self.layout.addLayout(main_layout)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

