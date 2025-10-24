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
        layout = QVBoxLayout()
        album = Album()

        layout.addWidget(album)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class Album(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout()

        self.setLayout(main_layout)
        self.show()
