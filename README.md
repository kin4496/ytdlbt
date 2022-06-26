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
from ytdlbt import ytdlbt as yt

yt.download('loststarts')
```

### Usage
````
#get url
url= yt.get_url('loststars')

#download

path='./'
yt.download('loststarts',path)
#download mp3 file by song title

yt._download(url,path)
#download mp3 file by url
