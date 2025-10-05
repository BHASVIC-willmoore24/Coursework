from mutagen import (
    flac,
    MutagenError,
)

import os

directory = "/home/will/Music/"

song_paths = []

def scan_dir(path):
    dir = os.scandir(path)
    for i in dir:
        if i.is_dir():
            scan_dir(i.path)
        else:
            song_paths.append(f"{i.path}")
        

scan_dir(directory)

print(song_paths)

test = flac.FLAC(song_paths[0])
print(test["ARTIST"])

