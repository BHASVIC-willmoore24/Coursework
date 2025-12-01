from PySide6.QtWidgets import (
        QMainWindow,
        QWidget,
        QVBoxLayout,
        QLabel,
        QTextEdit
)

class Recommendations(QMainWindow):
    def __init__(self, stored_music):
        super().__init__()
        self.layout = QVBoxLayout()
        self.stored_music = stored_music

        self.recs = QTextEdit()
        self.recs.setReadOnly(True)
        self.recs.setPlaceholderText("No track playing")

        self.layout.addWidget(self.recs)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def get_recommendations(self, current_track, artist, album, genre):
        # list for scored tracks
        scored = []

        # gets full track info
        library = self.stored_music.get_metadata()

        for track in library:
            score = 0

            # give each track a score based on how close close it is
            # same artist
            if track[1] == current_track[1]:
                score += 1
            
            # lowers score for same album otherwise entire recommendations would all be from same album
            if track[2] == current_track[2]:
                score -= 3

            # same genre - might not be as consistent as dependent on tags
            if track[6] == current_track[6]:
                score += 2

            if score > 0:
                scored.append([score, track])

        # sort by score
        sorted_scored = sorted(scored, key=lambda x: x[0])
        # only give top ten results
        top_ten = sorted_scored[0:10]

        self.recs.setText(f"{str(sorted_scored)}")

