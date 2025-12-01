from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTabWidget,
)


class LeftPane(QMainWindow):
    def __init__(self, library, lyrics, credit, settings, recommendations):
        super().__init__()
        layout = QVBoxLayout()

        # tab widget will make the left pane show a single widget that can be swapped using a tab bar
        self.tab_bar = QTabWidget()
        self.tab_bar.addTab(library, "Library")
        self.tab_bar.addTab(lyrics, "Lyrics")
        self.tab_bar.addTab(credit, "Credits")
        self.tab_bar.addTab(recommendations, "Recommendations")
        self.tab_bar.addTab(settings, "Settings")

        layout.addWidget(self.tab_bar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
