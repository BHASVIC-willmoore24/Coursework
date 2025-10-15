from mutagen import (
    flac,
    mp3,
)


class StoredMusic:
    def __init__(self):
        self.song_paths = []

    def append_song_paths(self, path):
        self.song_paths.append(path)

    def clear_song_paths(self):
        self.song_paths = []
