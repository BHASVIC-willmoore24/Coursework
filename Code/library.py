from PySide6.QtWidgets import (
    QPushButton,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
)

from stored_music import StoredMusic


class Library(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stored_music = StoredMusic()

    def update_library(self):
        main_layout = QVBoxLayout()
        count = self.stored_music.num_tracks()

        albums = []

        for i in range(count):
            album_layout = QHBoxLayout()

            if self.stored_music.get_metadata(i, 2) in albums:


            album = QWidget()
            album.setLayout(album_layout)
            main_layout.addWidget(album)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
