import mutagen
import os

class StoredMusic:
    def __init__(self):
        self.song_paths = []  # list for song paths only
        self.tracks_full = []  # 2D list, full metadata

    def append_song_paths(self, path):
        self.song_paths.append(f"{path}")
        self.read_metadata(f"{path}")

    def clear_song_paths(self):
        self.song_paths = []
        self.tracks_full = []

    def read_metadata(self, path):
        data = mutagen.File(path)

        if data:
            temp_list = [0] * 9
            temp_list[0] = path
            temp_list[1] = data["artist"]
            temp_list[2] = data["album"]
            temp_list[3] = data["title"]
            temp_list[4] = data["tracknumber"]
            temp_list[5] = data["date"]
            temp_list[6] = data["genre"]
            temp_list[7] = data.info.length
            temp_list[8] = self.album_cover(path)

            self.tracks_full.append(temp_list)

    def album_cover(self, path):
        dir_path = os.path.dirname(path)
        dir_contents = os.scandir(dir_path)

        for i in dir_contents:
            file = os.path.splitext(i)
            name = file[0]
            ext = file[1]
            if ext == ".png" or ext == ".jpg":
                return name + ext

    def get_metadata(self):
        return self.tracks_full

    def num_tracks(self):
        return len(self.tracks_full)
