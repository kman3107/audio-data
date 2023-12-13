"""
This will read the files in the cwd into a list, then read the filenames
Split the filenames into artist and title and add them to the metadata
"""

from mutagen.easymp4 import EasyMP4
import glob


class AudioFiles:
    def __init__(self):
        self.music_files = []
        self.music_artist = ""
        self.music_title = ""

    def set_metadata(self):
        for files in glob.glob("*.m4a"):
            self.music_files.append(files)

        for i in self.music_files:
            audiofile = EasyMP4(i)
            artist_title = i.split(" - ", 1)
            artist = artist_title[0]
            title = artist_title[1][:len(artist_title[1])-15]

            audiofile["artist"] = f"{artist}"
            audiofile["title"] = f"{title}"
            # print(audiofile.tags)
            audiofile.save()


Janitor = AudioFiles()
Janitor.set_metadata()
