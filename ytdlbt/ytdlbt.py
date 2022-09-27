from youtubesearchpython import *
from pytube import YouTube as yt

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

import os

YOUTUBE_LINK_BASE="https://youtube.com{}"

def preprocess(title,artist):
    
    if isinstance(artist,list):
        if len(artist)!=0:
            artist=''
        else:
            artist=artist[0]
    
    if artist == None or artist=='':
        text=title
    else:
        text=f"{artist} {title}"
    
    return text

def search(title,artist,uploadDate=False,viewCount=False,rating=False):

    query=preprocess(title,artist)
    
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
    fname=base+'.wav'
    os.rename(music,fname)

    return fname

def transform(path,fname,title,artist,deleted=False):
    
    path = os.path.join(path,fname)
    y,sr = librosa.load(path)
    duration = len(y) // sr
    half= duration//2
    y=y[half*sr:(half+30)*sr]
    
    S=librosa.feature.melspectrogram(y=y, sr=sr)
    S_dB = librosa.power_to_db(S,ref=np.max)
    librosa.display.specshow(S_dB,sr=sr)
    fname=preprocess(title,artist)
    plt.savefig(fname+'.jpg',format='jpg')

    if deleted:
        os.remove(path)


if __name__=="__main__":

    titles=['밤편지','좋은날','예술이야']
    artist=['아이유','아이유','싸이']

    for title,artist in zip(titles,artist):

        url=search(title,artist)
        fname=download(url)
        transform('./',fname,title,artist)
