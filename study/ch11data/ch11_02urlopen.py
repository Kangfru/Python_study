import urllib.request

url = 'http://uta.pw/shodou/img/28/214.png'
savename = 'test.png'

mem = urllib.request.urlopen(url).read()

# with 문으로 선언된 객체는 with문 밖으로 나가면서 close() 됨
with open(savename, mode = "wb") as f:
    f.write(mem)
    print("저장")