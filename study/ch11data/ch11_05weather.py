import urllib.request
import urllib.parse

API = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# json 형식으로 파라메터를 보냄
values = {
    'stnId' : '108'
}

params = urllib.parse.urlencode(values)

# 요청전용 url 생성
url = API + "?" + params
print("url=", url)

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)