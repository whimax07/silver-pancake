from Code_Base import codeBase2
from Code_Base import codeBase3

plURLs = codeBase2.Playlist('https://www.youtube.com/playlist?list=PL5FF1BC4B5D7CE403')

plURLs.Playlist_all()
playlistURLS = plURLs.video_urls

for i in range(len(playlistURLS)):
    videoDetails = codebase3.YouTube()
    videoDetails.url = playlistURLS[i] 
    

print('It works')