from youtubesearchpython import *
from pytube import YouTube as yt

import os

YOUTUBE_LINK_BASE="https://youtube.com{}"

def search(title,artist,uploadDate=False,viewCount=False,rating=False):

    if isinstance(artist,list):
        if len(artist)!=0:
            artist=''
        else:
            artist=artist[0]
    
    if artist == None or artist=='':
        query=title
    else:
        query=f"{artist} {title}"
    
    if uploadDate:
        filter=VideoSortOrder.uploadDate
    elif viewCount:
        filter=VideoSortOrder.viewCount
    elif rating:
        filter=VideoSortOrder.rating
    else:
        filter=None
    
    if filter != None:
        video=CustomSearch(query=query,searchPreferences=filter,limit=1).result()["result"]
    else:
        video=VideosSearch(query=query,limit=1).result()["result"]

    if video == None or len(video)==0:
        print('음원을 찾지 못했습니다.')
        return None

    video=video[0]

    url=f"/watch?v={video['id']}"
    url=YOUTUBE_LINK_BASE.format(url)
    
    return url

def download(url,path='./',progressive=None,adaptive=None,only_audio=True,file_extension=None):
    
    if url==None:
        print('주소 값이 없습니다.')
        return None

    music = yt(url)
    music_stream = music.streams.filter(progressive=progressive,adaptive=adaptive,
                    only_audio = only_audio,file_extension=file_extension).first()
    
    if music_stream == None:
        print('음악을 찾을 수 없습니다.')
        return None

    music=music_stream.download(output_path=path)
    base , ext = os.path.splitext(music)
    fname=base+'.mp3'
    os.rename(music,fname)

    return fname


if __name__=="__main__":
    url=search('좋은날','아이유')
    download(url)
