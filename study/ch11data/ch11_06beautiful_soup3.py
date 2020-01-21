from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href = "http://www.naver.com">naver</a></li>
        <li><a href = "http://www.daum.net">daum</a></li>
    </ul>
</body></html>
"""

list_links = []

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")

# find() -> object find_all() -> [object, ...] : list


for a in links:
    data = {}
    href = a.attrs['href']
    text = a.string
    data["site"] = text
    data["url"] = href
    print(text, ">", href)
    list_links.append(data)

print(list_links)