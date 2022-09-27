# Youtube Downloader By Title

Downlaod music from Youtube by song title

### PypI
```
pip3 install ytdlbt
```

### Quick start
```
pip3 install ytdlbt
```

```
titles=['밤편지','좋은날','예술이야']
artist=['아이유','아이유','싸이']

path='./'

for title,artist in zip(titles,artist):
  url=yt.search(title,artist)
  fname=yt.download(url)  
  yt.transform(path,fname,title,artist)
  #yt.transform(path,fname,title,artist,deleted=True)
  #다운받은 음악파일을 삭제한다. 
```
