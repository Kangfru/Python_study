# 실습전에 한빛 미디어 회원가입을 해주세요

import  requests
from bs4 import BeautifulSoup

USER = "kwooooook"
PASS = "PT7!CpCDyChxAXJ"

session = requests.session()

# form tag 안 input tag 의 name을 확인 후 작성
login_info = {
    "m_id" : USER,
    "m_passwd" : PASS
}

# post 방식으로 전송(JSON) -> action 속성값
# 아이디와 비밀번호를 받아서 로그인 처리를 해주는 프로그램
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data = login_info)
res.raise_for_status()

url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("마일리지 : " + mileage)
print("이코인 : " + ecoin)
