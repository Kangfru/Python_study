from bs4 import BeautifulSoup
import urllib.request as req
url = "https://finance.naver.com/marketindex/"
# euc-kr 엔코딩해서 불려온다.
res = req.urlopen(url)
# 한글 utf-8로 처리 : 원래 데이터가 euc-kr
soup = BeautifulSoup(res, "html.parser", from_encoding="euc-kr")

# print(soup)

price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)

datas = soup.select(".data_lst > li")
# print(datas)
for d in datas:
    # 국가/나라
    print(d.select_one(".h_lst > .blind").string)
    # 환율
    print(d.select_one(".value").string)

