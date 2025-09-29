from mutagen import (
    flac,
    MutagenError,
)

import os

directory = "Either_Or"

dir_list = os.listdir(directory)

test = flac.FLAC(f"{directory}/{dir_list[0]}")

test.pprint()
