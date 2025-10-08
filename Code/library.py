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


class Library(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        choose_dir = QPushButton("Select Music Folder")
        choose_dir.clicked.connect(self.file_dialog)
        self.current_dir = QLineEdit()

        layout.addWidget(self.current_dir)
        layout.addWidget(choose_dir)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def file_dialog(self):
        directory = QFileDialog.getExistingDirectory(self, "Choose directory")
        if directory:
            self.current_dir.setText(f"{directory}")
