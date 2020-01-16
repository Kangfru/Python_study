ss = "파이썬을 열심히 공부하는 중"
print(ss)
print(ss.split())

ss = "하나:둘:셋"
print(ss, type(ss))
print(ss.split(':'), type(ss.split(':')))

# 전화번호 3개 -> 010-1111-2222
tel = "010-1111-2222".split("-")
print('첫째 자리 %s 둘째 자리 %s 셋째 자리 %s' %(tel[0], tel[1], tel[2]))

# 분리되어있는 데이터를 중간에 "-"를 이용해 전화번호 출력
print("-".join(tel))

# 정렬 : 가운데, 왼쪽, 오른쪽, 채우기
ss = "파이썬"
print("[", end="")
print(ss.center(10), end="")
print("]")
print("[", end="")
print(ss.center(10, "-"), end="")
print("]")
print("[", end="")
print(ss.ljust(10), end="")
print("]")
print("[", end="")
print(ss.rjust(10), end="")
print("]")
print("[", end="")
print(ss.zfill(10), end="")
print("]")
