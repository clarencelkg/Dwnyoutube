from pytubefix import YouTube

def Download(link):
    yt = YouTube(link) # To get the Youtube Object
    youtubeObject = yt.streams.get_highest_resolution() # Get highest resolution stream that is a progressive video.
    try:
        youtubeObject.download() # Write the media stream to disk.
    except:
        print("An error has occurred")
    print("Download is completed successfully")

link = input("Enter the URL of the video: ")
Download(link)
