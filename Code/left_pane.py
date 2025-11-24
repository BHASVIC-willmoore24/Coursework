from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTabWidget,
)


class LeftPane(QMainWindow):
    def __init__(self, library, lyrics, credit, settings):
        super().__init__()
        layout = QVBoxLayout()

        self.tab_bar = QTabWidget()
        self.tab_bar.addTab(library, "Library")
        self.tab_bar.addTab(lyrics, "Lyrics")
        self.tab_bar.addTab(credit, "Credits")
        self.tab_bar.addTab(settings, "Settings")

        layout.addWidget(self.tab_bar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
