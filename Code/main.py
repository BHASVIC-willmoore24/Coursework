from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTabWidget,
    QLabel,
)

from mutagen import (
    flac,
    mp3,
)

import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setMinimumSize(800, 600)
        main_layout = QHBoxLayout()  # main layout will be two horizontal panes
        left_pane = LeftPane()
        right_pane = RightPane()

        main_layout.addWidget(left_pane)
        main_layout.addWidget(right_pane)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


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


class Library(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class Lyrics(QMainWindow):
    def __init__(self):
        super().__init__()


class Credits(QMainWindow):
    def __init__(self):
        super().__init__()


class RightPane(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.play_button = QPushButton("Paused")
        self.play_button.setCheckable(True)  # button can be toggled
        self.play_button.clicked.connect(self.play_pause)

        layout.addWidget(self.play_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def play_pause(self, checked):
        if checked:
            self.play_button.setText("Playing")
        else:
            self.play_button.setText("Paused")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
