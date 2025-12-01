from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLabel
)

# musicbrainzngs is the Python bindings for the musicbrainz API
import musicbrainzngs
musicbrainzngs.set_useragent("Music Player", "1", "test")
musicbrainzngs.set_rate_limit(limit_or_interval=5)

class Credits(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.credits = QTextEdit()
        self.credits.setReadOnly(True)
        self.credits.setPlaceholderText("Credits not available")

        self.layout.addWidget(self.credits)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    # main method that uses the API
    def searching(self, artist_id):
        # using try and except, because getting data from database is not consistent and errors are frequent
        try:
            data = musicbrainzngs.browse_artists(recording=artist_id, includes=["artist-rels"], limit=100)
            credits_info = self.parse_credits(data)
            self.credits.setText(credits_info)
        except Exception as error:
            self.credits.setText(f"Error fetching credits, {str(error)}")

    # API request returns a dictionary, which needs to be formatted into being more readable
    def parse_credits(self, data):
        #list here will contain each person/artist linked to this track, and the instrument they play
        people_and_instruments = []

        for artist in data["artist-list"]:

            for link in artist.get("artist-relation-list", []):
                artist_info = link.get("artist", {})
                attributes = link.get("attribute-list", [])

                if artist_info and attributes:
                    name = artist_info.get("name")
                    instruments = [attribute for attribute in attributes]

                    if name and instruments:
                        people_and_instruments.append({
                            "name": name,
                            "instruments": instruments
                        })

        # readable format
        if people_and_instruments:
            credit_strings = []
            for i in people_and_instruments:
                instruments_str = ", ".join(i["instruments"]).capitalize()
                credit_strings.append(f"{i["name"]} ({instruments_str})")
            # new line
            return "\n".join(credit_strings)
        else:
            return "Could not get credits"

