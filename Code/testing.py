from mutagen import (
    flac,
)

import os


def scandir(path):
    current_dir = os.scandir(path)
    for i in current_dir:
        if i.is_dir():
            scandir(i.path)
        else:
            song_paths.append(f"{i.path}")


directory = "../Music/"

song_paths = []

scandir(directory)

print(song_paths[0])

test = flac.FLAC(song_paths[0])
print(test["ARTIST"])
