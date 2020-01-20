# 1. 214.png 파일을 test.png로 다운로드하기
import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

urllib.request.urlretrieve(url, savename)
print('완료')

# 2. 다운로드 받고자하는 이미지파일으 찾아서 다운로드하기
url = "https://s3.ap-northeast-2.amazonaws.com/img.kormedi.com/news/article/__icsFiles/artimage/2018/01/31/c_km601/650445_540.jpg"
savename = "down.jpg"

urllib.request.urlretrieve(url, savename)
print('완료')
