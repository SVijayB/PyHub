from pytube import YouTube
from pytube import Playlist

# Downloading a single video.
YouTube('https://youtu.be/DveVvg3A-dI').streams.first().download()

# Downloading a playlist.
PL = Playlist("https://www.youtube.com/playlist?list=PL0yKcKIX3z44V9vjj-hGVpIYyK70t1eI6")
for video in PL.videos:
    video.stream.first().download()

# Downloading just the audio
YouTube('https://youtu.be/XqZsoesa55w').streams.first().filter(only_audio=True).download()