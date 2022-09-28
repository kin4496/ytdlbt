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

### Usage

#### search(title,artist,uploadDate=False,viewCount=False,rating=False)
```

  매개변수
  title : 노래 제목,
  artist : 가수(만약 None값이 들어가면 제목만 가지고 검색),
  uploadDate : True일시 업로드된 시간을 기준으로 가져옴,
  viewCount : True일시 조회수 기준으로 가져옴,
  rating : True일시 좋아요 기준으로 가져옴
  
  return
  유튜브 url 반환 없으면 None값 반환
```

#### download(url,path,fname,progressive=None,adaptive=None,only_audio=True,file_extension=None)
```

  매개변수
  url : search 반환한 유튜브 주소를 넘겨준다.
  path , fname : 음원을 저장할 위치와 파일 이름
  
  return 
  다운로드 한 음원의 파일 이름을 반환한다. 다운로드 실패시 None값 반환
  
```

#### transform(path,fname,title,artist,deleted=False)
```

  매개변수
  path, fname : 음원이 저장된 위치와 파일 이름
  title,artist : 멜스펙트럼을 저장할때 쓰일 제목과 가수 정보(ex '아이유 밤편지') 이런 형태로 저장됨
  deleted : True일시 멜스펙트럼 변환 후 음원파일을 삭제
```

