from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QSizePolicy, QScrollArea, QPushButton,
)

from PySide6.QtGui import (
    QPixmap,
)

import PySide6.QtCore


class Library(QMainWindow):
    def __init__(self, right_pane):
        super().__init__()
        self.layout = QVBoxLayout()
        self.right_pane = right_pane

    # using a method to update library display so this can be called in other classes
    def update_library(self, track):
        main_layout = QVBoxLayout()
        size_policy = QSizePolicy()
        size_policy.setVerticalPolicy(QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalPolicy(QSizePolicy.Policy.Fixed)

        # if statement ensures only working on a list - so there is no error during loop
        if len(track) > 0:

            # loop through each track - each sub list
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
                cover.setSizePolicy(size_policy)
                album_layout.addWidget(cover)

                title = QLabel(self)
                title.setText(" ".join(track[i][3]))
                title.setSizePolicy(size_policy)
                info_layout.addWidget(title)

                album = QLabel(self)
                album.setText(" ".join(track[i][2]))
                album.setSizePolicy(size_policy)
                info_layout.addWidget(album)

                artist = QLabel(self)
                artist.setText(" ".join(track[i][1]))
                artist.setSizePolicy(size_policy)
                info_layout.addWidget(artist)

                play_track = QPushButton(self)
                play_track.setText("Play")
                info = track[i]
                play_track.clicked.connect(lambda: self.track_info(info))
                play_track.setSizePolicy(size_policy)

                album_layout.addLayout(info_layout)
                album_layout.addWidget(play_track)
                main_layout.addLayout(album_layout)

        self.layout.addLayout(main_layout)

        widget = QWidget()
        scroll_area = QScrollArea()
        scroll_area.setWidget(widget)
        scroll_area.setWidgetResizable(True)
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def track_info(self, trackinf):
        self.right_pane.current_track(trackinf)
