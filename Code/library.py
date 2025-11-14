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
        main_layout = QVBoxLayout()
        self.stored_music = StoredMusic()

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
    
    def update_library(self, tracks):
        album_layout = QHBoxLayout()
        play_button = QPushButton("Paused")
        album_layout.addWidget(play_button)

        for i in range(len(tracks)):
            cover = QLabel(self)
            cover_path = tracks[i][8]
            pixmap = QPixmap(cover_path)
            cover.setPixmap(pixmap)
            album_layout.addWidget(cover)

        widget = QWidget()
        widget.setLayout(album_layout)
        self.setCentralWidget(widget)
        
