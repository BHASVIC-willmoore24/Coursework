import mutagen

test = mutagen.File("../Music/Elliott Smith/Either_Or/04 - between the bars.flac")
#test = mutagen.File("config.ini")
if test:
    print(test.pprint())
    print(test.info.length)
