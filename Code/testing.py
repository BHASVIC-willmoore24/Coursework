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
)

from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setMinimumSize(100, 100)
        main_layout = QHBoxLayout()  # main layout will be two horizontal panes

        label = QLabel(self)
        pixmap = QPixmap("C:/Users/will.moore24/Downloads/Coursework/Coursework/Music/Elliott Smith/Either_Or/cover.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        main_layout.addWidget(label)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
