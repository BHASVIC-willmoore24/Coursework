from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
)

from left_pane import LeftPane
from right_pane import RightPane
from library import Library
from lyrics import Lyrics
from credits import Credits
from settings import Settings
from stored_music import StoredMusic
from recommendations import Recommendations


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setMinimumSize(800, 600)
        main_layout = QHBoxLayout()  # main layout will be two horizontal panes

        # instantiating objects
        lyrics = Lyrics()
        credit = Credits()
        stored_music = StoredMusic()
        recommendations = Recommendations(stored_music)
        right_pane = RightPane(lyrics, credit, recommendations)
        library = Library(right_pane)
        settings = Settings(library, stored_music)
        left_pane = LeftPane(library, lyrics, credit, settings, recommendations)

        main_layout.addWidget(left_pane)
        main_layout.addWidget(right_pane)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
