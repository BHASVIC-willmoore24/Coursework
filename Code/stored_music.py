import mutagen


class StoredMusic:
    def __init__(self):
        self.song_paths = []
        self.tracks_full = []

    def append_song_paths(self, path):
        self.song_paths.append(f"{path}")
        self.read_metadata(f"{path}")

    def clear_song_paths(self):
        self.song_paths = []

    def read_metadata(self, path):
        data = mutagen.File(path)

        if data:
            temp_list = [0] * 8
            temp_list[0] = path
            temp_list[1] = data["artist"]
            temp_list[2] = data["album"]
            temp_list[3] = data["title"]
            temp_list[4] = data["tracknumber"]
            temp_list[5] = data["date"]
            temp_list[6] = data["genre"]
            temp_list[7] = data.info.length

            self.tracks_full.append(temp_list)

    def get_metadata(self, index, data):
        return self.tracks_full[index][data]
