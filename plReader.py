from Code_Base import codeBase2 as cb2
from Code_Base import codeBase3 as cb3

plURLs = cb2.Playlist('https://www.youtube.com/playlist?list=PL5FF1BC4B5D7CE403')

plURLs.Playlist_all()
playlistURLS = plURLs.video_urls

for i in range(len(playlistURLS)):
    videoDetails = cb3.YouTube(playlistURLS[i])
    

print('It works')