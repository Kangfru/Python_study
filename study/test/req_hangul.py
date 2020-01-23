import urllib.request
url = "http://cafe.naver.com/pystock"
print("url=", url)
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
