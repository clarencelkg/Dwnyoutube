from pytubefix import YouTube
from pytubefix.cli import on_progress

link = "https://www.youtube.com/watch?v=s1h_9uNrqlw"
#Download aand display download progress
yt = YouTube(link, on_progress_callback = on_progress) 
print("Title :", yt.title)
print("Views :", yt.views)
print("Description :", yt.description)
stream = yt.streams.get_highest_resolution()
stream.download()
print("Download Done!!")
