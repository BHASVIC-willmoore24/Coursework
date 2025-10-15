from PySide6.QtWidgets import (
    QPushButton,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QFileDialog,
    QLineEdit,
)


class Library(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

