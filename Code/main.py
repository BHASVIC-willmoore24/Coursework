from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTabWidget,
    QLabel,
    QFileDialog,
    QLineEdit,
)

from left_pane import LeftPane
from right_pane import RightPane


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


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
