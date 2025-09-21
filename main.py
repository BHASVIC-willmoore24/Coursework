from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStackedLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")

        layout = QHBoxLayout()

        self.play_button = QPushButton("Paused")
        self.play_button.setCheckable(True)
        self.play_button.clicked.connect(self.play_pause)

        layout.addWidget(self.play_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def play_pause(self, checked):
        if checked == True:
            self.play_button.setText("Playing")
        else:
            self.play_button.setText("Paused")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
