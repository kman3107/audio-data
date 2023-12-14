"""
This will read all files in the cwd into a list, and open each file with mutagen if mp3, mp4 or m4a
Split the filenames into artist and title and add them to the metadata
"""
import re
import os
from mutagen.easymp4 import EasyMP4
from mutagen.easyid3 import EasyID3


class AudioFiles:
    def __init__(self, directory):
        os.chdir(directory)
        self.dir_w_files = directory
        self.music_files = []
        self.music_artist = ""
        self.music_title = ""
        self.artist_title = ""
        self.tags = []

    def set_metadata(self):
        for i, f in enumerate(os.listdir(self.dir_w_files)):
            if os.path.isfile(f):
                self.music_files.append(f)

        for i in self.music_files:
            if ".m4a" in i or ".mp4" in i:
                audiofile4 = EasyMP4(i)
                self.artist_title = i.split(" - ", 2)
                self.music_artist = self.artist_title[0]
                self.music_title = self.artist_title[1][:len(self.artist_title[1]) - 4]

                audiofile4["artist"] = f"{self.music_artist}"
                audiofile4["title"] = f"{self.music_title}"
                audiofile4.save()

            if ".id3" in i or ".mp3" in i:
                try:
                    audiofile3 = EasyID3(i)
                    self.artist_title = i.split(" - ", 2)
                    self.music_artist = self.artist_title[0]
                    self.music_title = self.artist_title[1][:len(self.artist_title[1]) - 4]

                    audiofile3["artist"] = f"{self.music_artist}"
                    audiofile3["title"] = f"{self.music_title}"
                    audiofile3.save()
                except ValueError:
                    pass

    def get_metadata(self):
        for i, f in enumerate(os.listdir(self.dir_w_files)):
            if os.path.isfile(f):
                self.music_files.append(f)

        for i in self.music_files:
            if ".id3" in i or ".mp3" in i:
                try:
                    audiofile3 = EasyID3(i)
                    self.tags.append(audiofile3)
                except ValueError:
                    pass
            if ".m4a" in i or ".mp4" in i:
                audiofile4 = EasyMP4(i)
                self.tags.append(audiofile4)
        return self.tags

    def prepend(self, prep):
        for i, f in enumerate(os.listdir(self.dir_w_files)):
            if os.path.isfile(f):
                src = os.path.join(self.dir_w_files, f)
                dst = os.path.join(self.dir_w_files, f"{prep}{f}")
                os.rename(src, dst)

    def remove_substr(self, substr):
        for i, f in enumerate(os.listdir(self.dir_w_files)):
            if os.path.isfile(f):
                src = os.path.join(self.dir_w_files, f)
                dst = os.path.join(self.dir_w_files, re.sub(f"{substr}.*?", "", f))
                os.rename(src, dst)
