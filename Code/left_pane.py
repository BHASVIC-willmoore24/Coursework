from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTabWidget,
)

from library import Library
from lyrics import Lyrics
from credits import Credits


class LeftPane(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.tab_bar = QTabWidget()
        self.tab_bar.addTab(Library(), "Library")
        self.tab_bar.addTab(Lyrics(), "Lyrics")
        self.tab_bar.addTab(Credits(), "Credits")

        layout.addWidget(self.tab_bar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
