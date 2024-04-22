"""
This will read all files in the cwd into a list, and open each file with mutagen if mp3, mp4 or m4a
Split the filenames into artist and title and add them to the metadata
"""
import os
import re

import mutagen.id3
from mutagen.easyid3 import EasyID3
from mutagen.easymp4 import EasyMP4


class AudioFiles:
    def __init__(self, directory):
        os.chdir(directory)
        self.dir_w_files = directory
        self.music_files = []
        self.id3_list = [".id3", ".mp3"]
        self.mp4_list = [".m4a", "mp4"]
        self.music_artist = ""
        self.music_title = ""
        self.artist_title = ""
        self.get_tags = []
        self.easy_file = None

    def set_metadata(self):
        for i, f in enumerate(os.listdir(self.dir_w_files)):
            if os.path.isfile(f):
                self.music_files.append(f)

        for i in self.music_files:
            self.artist_title = i.split(" - ", 2)
            self.music_artist = self.artist_title[0]
            self.music_title = self.artist_title[1][:len(self.artist_title[1]) - 4]
            self.set_tags(i, title=self.music_title, artist=self.music_artist)

    def set_tags(self, file_path, title=None, artist=None):
        if file_path[-4:] in self.id3_list:
            try:
                self.easy_file = EasyID3(file_path)
                self.easy_file['title'] = title
                self.easy_file['artist'] = artist
                self.easy_file.save()
            except mutagen.id3.ID3NoHeaderError as e:
                print(f"EasyMP3: {e}")
                pass
        if file_path[-4:] in self.mp4_list:
            try:
                self.easy_file = EasyMP4(file_path)
                self.easy_file['title'] = title
                self.easy_file['artist'] = artist
                self.easy_file.save()
            except mutagen.id3.ID3NoHeaderError as e:
                print(f"EasyMP4: {e}")
                pass

    def get_metadata(self):
        # TODO - use pprint to get tags, this way I can make it look a bit better
        for i, f in enumerate(os.listdir(self.dir_w_files)):
            if os.path.isfile(f):
                self.music_files.append(f)

        for i in self.music_files:
            if i[-4:] in self.id3_list:
                try:
                    self.easy_file = EasyID3(i)
                    self.get_tags.append(self.easy_file)
                except mutagen.id3.ID3NoHeaderError as e:
                    print(f"EasyMP3: {e}")
                    pass
            if i[-4:] in self.mp4_list:
                try:
                    self.easy_file = EasyMP4(i)
                    self.get_tags.append(self.easy_file)
                except mutagen.id3.ID3NoHeaderError as e:
                    print(f"EasyMP4: {e}")
        return self.get_tags

    def append(self, prep):
        for i, f in enumerate(os.listdir(self.dir_w_files)):
            if os.path.isfile(f):
                src = os.path.join(self.dir_w_files, f)
                file_ext = os.path.splitext(f)
                dst = os.path.join(self.dir_w_files, f"{file_ext[0]}{prep}{file_ext[1]}")
                os.rename(src, dst)

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
