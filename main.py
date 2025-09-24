from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
    QTabWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")

        main_layout = QHBoxLayout()  # main layout will be two horizontal panes
        left_pane = QStackedLayout()
        right_pane = QVBoxLayout()

        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)

        library = Library()
        now_playing = NowPlaying()

        left_pane.addWidget(library)
        right_pane.addWidget(now_playing)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


class LeftPane(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        tab_bar = QTabWidget()
        tab_bar.addTab("Library")
        tab_bar.addTab("Now Playing")

        layout.addWidget(tab_bar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class Library(QMainWindow):
    def __init__(self):
        super().__init__()


class NowPlaying(QMainWindow):
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
