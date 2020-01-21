from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# json 형식으로 파라메터를 보냄

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")
locations = soup.find_all("location")

for location in locations:
    datas = location.find_all("data")
    for city in location.find_all("city"):
        print("---------------%s---------------" %(city.string))
        for data in datas:
            print("날짜", data.find('tmef').text)
            print("날씨", data.find('wf').text)
            print("최저 기온", data.find('tmn').text)
            print("최고기온", data.find('tmx').text)
            print("강우확률", data.find('rnst').text)
