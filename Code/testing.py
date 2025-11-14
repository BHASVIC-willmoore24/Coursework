"""
import mutagen

test = mutagen.File("../Music/Elliott Smith/Either_Or/04 Between the Bars.flac")
#test = mutagen.File("config.ini")
if test:
    print(test.pprint())
    print(test.info.length)
"""

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QLabel,
    QPushButton,
)

from PySide6.QtGui import QPixmap

from stored_music import StoredMusic

from settings import Settings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def addwidge(self):
        layout = QHBoxLayout()
        play_button = QPushButton("Paused")
        layout.addWidget(play_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
       

class tester():
    def __init__(self):
        super().__init__()
        testimp = MainWindow()
        testimp.addwidge()


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
