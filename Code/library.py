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

from stored_music import StoredMusic


class Library(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.stored_music = StoredMusic()

        self.update_library()

        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    def update_library(self):
        count = self.stored_music.num_tracks()

        albums = []

        for i in range(count):
            album_layout = QHBoxLayout()

            if self.stored_music.get_metadata(i, 2) not in albums:
                temp_list = []
                temp_list = self.stored_music.get_metadata(i, 2), i
                albums.append(temp_list)
            else:
                index = albums.index(self.stored_music.get_metadata(i, 2))
                albums[index].append(i)

            cover = QLabel(self)
            cover_path = self.stored_music.get_metadata(i, 8)
            pixmap = QPixmap(cover_path)
            cover.setPixmap(pixmap)
            album_layout.addWidget(cover)

            album = QWidget()
            album.setLayout(album_layout)
            self.main_layout.addWidget(album)

"""
        test_layout = QHBoxLayout()
        label = QLabel(self)
        pixmap = QPixmap("C:/Users/will.moore24/Downloads/Coursework/Coursework/Music/Elliott Smith/Either_Or/cover.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        test_layout.addWidget(label)
        test = QWidget()
        test.setLayout(test_layout)
        self.main_layout.addWidget(test)
"""