# "https://docs.python.org/3.5/library/" 연결되어 있는 파일 다운로드

from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path
import time
import re

# 다운로드 받은 페이지 저장
proc_files = {}


# 링크의 페이지를 찾는 함수
# enum_links(분석해야할 html 문서, 다운로드 받은 페이지)
def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    # css 링크 추가 -> 객체 리스트
    links = soup.select("link[rel='stylesheet']")
    # a 링크 추가 -> 위의 객체 리스트에 리스트를 추가
    links += soup.select("a[href]")
    # 링크 페이지(links:태그)를 절대 주소로 받아서 추가 시키는 리스트
    result = []
    for a in links:
        # 링크 걸린 url을 가져오기
        href = a.attrs['href']
        # 가져온 url를 절대 주소로 변환
        url = urljoin(base, href)
        # result에 추가 -> 가져와야할 페이지 저장
        result.append(url)
    return result


# 파일로 다운로드 받아내는 함수
# url은 다운로드 받아야할 절대 페이지
def download_file(url):
    o = urlparse(url)
    # 내 컴퓨터의 위치 정한다. -> 파일포함.
    # "./" -> 실행되고 있는 현재 -> ch11data/
    # o.netloc -> 서버의 위치(docs.python.org)
    # o.path -> 서버 뒤에 있는 내용
    savepath = "./" + o.netloc + o.path
    # savepath의 내용의 "/" 로 끝나면 페이지가 없다.-> 기본페이지(index.html) 추가
    if re.search(r"/$", savepath):
        savepath += "index.html"
    # 저장 폴더가 있는지 확인하기 위해서 폴더를 찾아낸다.
    savedir = os.path.dirname(savepath)
    # 폴더가 존재하면 이미 처리한 것으로 추정해서 바로 리턴한다.
    if os.path.exists(savepath):
        return savepath
    # 폴더가 존재하지 않으면 폴더를 만들고 다운로드를 실행한다.
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        # 폴더 만들기 실행
        makedirs(savedir)
    try:
        print("download=", url)
        # 다운 로드 실행
        urlretrieve(url, savepath)
        # 다운 로드된 페이지이름을 출력하는 것을 확인하기 위해서 딜레이타임 지정
        time.sleep(0.05)
        # 다운로드된 페이지 이름을 돌려준다.
        return savepath
    except:
        print("다운 실패: ", url)
        return None


# html 페이지 분석 함수 analyze_html(분석하려는 페이지, base)
def analyze_html(url, root_url):
    # 분석하려는 페이지 -> downloand_file함수 호출다운로드 받는다.
    savepath = download_file(url)
    # 다운로드 받은 페이지가 없다. -> 다운로드를 다 받았다.
    if savepath is None:
        return
    # 다운로드를 받을 페이지에 존재하면 리턴
    if savepath in proc_files:
        return
    # proc_files -> 다운받은 페이지를 키로 해서 저장한다.
    proc_files[savepath] = True
    # 다운로드 받는 페이지 분석
    print("analyze_html=", url)
    # html로 읽어오기 -> 다운로드된 파일을 읽기전용으로 열고 전체를 읽어온다.
    html = open(savepath, "r", encoding="utf-8").read()
    # 다운로드 받은 페이지에 링크가 걸려있는 목록을 가져온다. enum_links()호출
    links = enum_links(html, url)
    for link_url in links:
        # link_url.find(root_url) != 0 -> link_url이 root_url로 시작하지 않는다.
        if link_url.find(root_url) != 0:
            # link_url이 .css로 끝나지 않는다. -> css 파일이 아니다.
            if not re.search(r".css$", link_url):
                continue
        # link_url의 페이지가 html이나 htm 인경우는 다시 링크를 분석해야한다.
        if re.search(r".(html|htm)$", link_url):
            # 다운로드 받은 페이지가 html이나 html 경우 다시 분석실행
            analyze_html(link_url, root_url)
            continue
        # link_url가 html, htm이 아니고 다른 사이트의 url이 아닌 경우
        # 이미지 링크 같은 경우 - 다운로드
        download_file(link_url)


# 시작되는 부분
if __name__ == "__main__":
    # 다운로드 받고자하는 기본 페이지
    url = "https://docs.python.org/3.5/library/"
    # 페이지 분석 -> 기본페이지 분석 -> link를 리스트로 만든다. -> 다운받는다.
    analyze_html(url, url)
