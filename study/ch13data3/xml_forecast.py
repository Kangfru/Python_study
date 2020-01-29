from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# 데이터를 가져올 url -> 기상청에서 제공하고 있는 지역 날씨 예보 데이터
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
# 저장 파일명 -> 실행되는 위치에 저장
savename = "forecast.xml"
# 파일명이 존재하지 않는 경우 다운로드
if not os.path.exists(savename):
    # 다운로드 실행
    req.urlretrieve(url, savename)
# 다운로드 받은 파일을 읽기 전용으로 읽어 온다. -> 문자열
xml = open(savename, "r", encoding="utf-8").read()
# 구조로 가진 오브젝트로 만든다.
soup = BeautifulSoup(xml, 'html.parser')
# 표시할 정보가 들어 있는 딕셔너리 데이터
info = {}
# 모든 지역의 데이터 찾기
for location in soup.find_all("location"):
    name = location.find('city').string
    weather = location.find('wf').string
    if not (weather in info):
        info[weather] = []
    info[weather].append(name)

print(info)

# 날씨별 출력
for weather in info.keys():
    print("+", weather)
    # 날씨에 해당되는 지역 리스트
    for name in info[weather]:
        print("| - ", name)
