"""
This will read the m4a files in the cwd into a list, and open each file with mutagen
Split the filenames into artist and title and add them to the metadata
"""
import re
import os.path
from mutagen.easymp4 import EasyMP4


class AudioFiles:
    def __init__(self, directory):
        os.chdir(directory)
        self.dir_w_files = directory
        self.music_files = []
        self.music_artist = ""
        self.music_title = ""
        self.tags = []

    def set_metadata(self):
        for i, f in enumerate(os.listdir(self.dir_w_files)):
            self.music_files.append(f)

        for i in self.music_files:
            audiofile = EasyMP4(i)
            artist_title = i.split(" - ", 1)
            self.music_artist = artist_title[0]
            self.music_title = artist_title[1][:len(artist_title[1])-15]

            audiofile["artist"] = f"{self.music_artist}"
            audiofile["title"] = f"{self.music_title}"
            audiofile.save()

    def get_metadata(self):
        for i, f in enumerate(os.listdir(self.dir_w_files)):
            self.music_files.append(f)

        for i in self.music_files:
            audiofile = EasyMP4(i)
            self.tags.append(audiofile)
        return self.tags

    def prepend(self, prep):
        for i, f in enumerate(os.listdir(self.dir_w_files)):
            src = os.path.join(self.dir_w_files, f)
            dst = os.path.join(self.dir_w_files, f"{prep}{f}")
            os.rename(src, dst)

    def remove_substr(self, substr):
        for i, f in enumerate(os.listdir(self.dir_w_files)):
            src = os.path.join(self.dir_w_files, f)
            dst = os.path.join(self.dir_w_files, re.sub(f"{substr}.*?", "", f))
            os.rename(src, dst)
