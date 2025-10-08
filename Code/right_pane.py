from PySide6.QtWidgets import (
    QPushButton,
    QMainWindow,
    QWidget,
    QVBoxLayout,
)


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
