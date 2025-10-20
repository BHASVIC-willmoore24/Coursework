from mutagen import (
    flac,
    mp3,
)

import pathlib

class StoredMusic:
    def __init__(self):
        self.song_paths = []
        self.tracks_full = [[]]
        self.counter = 0

    def append_song_paths(self, path):
        self.song_paths.append(path)
        filetype = pathlib.Path(i.path).suffix
        self.read_metadata(path, filetype)

    def clear_song_paths(self):
        self.song_paths = []

    def read_metadata(self, path, filetype):
        if filetype == ".flac" or filetype == ".mp3":
            self.tracks_full[self.counter][0] = path
            self.tracks_full[self.counter][1] =

