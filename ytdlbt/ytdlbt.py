from youtubesearchpython import VideosSearch
from re import match
from typing import List
import os
from pytube import YouTube as yt

def get_url(name,useOpt=False,kw=[],lim=20):

    YOUTUBE_LINK_BASE="https://youtube.com{}"

    kw = [kw_ for kw_ in kw if kw_ is not None]

    if useOpt and len(kw):
        name += '+' + '+'.join(kw)
    
    # Replace all the spaces with +
    name = name.replace(' ', '+')

    results = VideosSearch(name, limit=lim).result()["result"]

    stripped_results = []

    for video in results:
        data = {}
        data['title'] = video['title']
        data['href'] = f"/watch?v={video['id']}"
        data['author_name'] = video['channel']["name"]
        data['duration'] = video['duration']
        stripped_results.append(data)
    
    return YOUTUBE_LINK_BASE.format(stripped_results[0]['href'])

def _download(url,path='./'):
    music = yt(url)
    music_stream = music.streams.filter(only_audio = True).first()
    music=music_stream.download(output_path=path)
    base , ext = os.path.splitext(music)
    os.rename(music,base+'.mp3')

def download(name,path='./'):
    url=get_url(name)
    _download(url,path)

