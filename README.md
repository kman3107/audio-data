# Edit MP3, MP4, and M4A
Just a tiny thing to help me have an easier time doing basic manual editing of new music files

# Front-end:
* CustomTkinter
* tkinter

# Back-end:
* mutagen (EasyMP4)
* mutagen (EasyID3)
* pillow
* re
* os
* sys

# The App
![empX_WD](https://github.com/kman3107/audio-data/assets/10728652/d794cdb8-4255-4cb6-8a20-4cf990956974)

When app is launched you need to give it the absolute path to the directory you will be working with (can only be done when app is launched).

![empX_app](https://github.com/kman3107/audio-data/assets/10728652/8433d0bf-1505-4cc8-98f2-cc8e0542db16)

This is the app after working directory has been given.

![empX_rem](https://github.com/kman3107/audio-data/assets/10728652/de36b489-1e9e-40fb-8a5b-d801f76c78a3)

Removing something from the filename can be done; even if that something is in the middle of the filename.

![empX_pre](https://github.com/kman3107/audio-data/assets/10728652/2cdb2b29-f544-4daf-92a4-5702a840c01d)

Here you can prepend some text to the filename.

![empX_set](https://github.com/kman3107/audio-data/assets/10728652/34909248-bdc4-4f19-b81b-2752aab7b53f)

Once you have the filename with something like 'Artist Name - Song Title.mp3', you can use that to set the artist and title tags.

![empX_get](https://github.com/kman3107/audio-data/assets/10728652/5194f8ad-5651-4d06-b7eb-422054395564)

To check if the tags are set you can use the get tag part of the app. Will show in popup as ['Title'] ['Artist']
NOTE! There is a limit to how many files tags you can see as the info box can not be scrolled.
