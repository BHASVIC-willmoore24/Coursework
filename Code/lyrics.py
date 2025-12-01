from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLabel
)
# allows for api requests from lrclib
import requests

class Lyrics(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.lyrics = QTextEdit()
        self.lyrics.setReadOnly(True)
        self.lyrics.setPlaceholderText("No track playing")

        self.layout.addWidget(self.lyrics)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    # main lyric getting method
    def searching(self, artist, title, album, duration):
        try:
            lrclib_parameters = {
                "artist_name": artist,
                "track_name": title,
                "album_name": album,
                # lrclib requires track duration to match, for accuracy
                "duration": duration
            }

            # initially had the timeout as 10, and it would often cause an error
            response = requests.get("https://lrclib.net/api/get", params=lrclib_parameters, timeout=60)
            if response.status_code == 200:
                data = response.json()
                # lrclib offers standard lyrics, or timestamped. Either works here
                lyrics = data.get("plainLyrics") or data.get("syncedLyrics") or "Lyrics not found"
                self.lyrics.setText(lyrics)
            else:
                search_lrclib_parameters = {"q": f"{artist} {title}"}
                response = requests.get("https://lrclib.net/api/search", params=search_lrclib_parameters, timeout=60)

                if response.status_code == 200:
                    data = response.json()
                    if data and isinstance(data, list) and len(data) > 0:
                        lyrics = data[0].get("plainLyrics") or data[0].get("syncedLyrics") or "Lyrics not found"
                        self.lyrics.setText(lyrics)
                    else:
                        self.lyrics.setText("Lyrics not found")
                else:
                    self.lyrics.setText("Lyrics not found")

        except Exception as error:
            self.lyrics.setText(f"Error fetching lyrics, {str(error)}")

