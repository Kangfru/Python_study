ss = '파이썬최고'

print(ss)
print(ss[1:3])

ss = '파이썬' + '최고!'
print(ss)
print(ss * 3)

print(len(ss))

# 문자열을 입력받아 역순출력
inStr = ""
count = 0
inStr = input("문자열읍 입력하세요.")
print(inStr)
count = len(inStr)

for i in range(count - 1, -1, -1):
    print(inStr[i], end = "")

print()
print(inStr[::-1])
print()

ss = 'Python is Easy. 그래서 Programming 재밌습니다.'
print(ss.upper())
print(ss.lower())
print(ss.swapcase())
print(ss.title())
