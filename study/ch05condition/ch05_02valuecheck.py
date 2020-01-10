a = 10
a = 0 # 숫자가 0인 경우 값이 없는 취급.
a = -10

if a:
    print('a는 값이 있다')
else:
    print('a는 값이 없다')

# s = ""  빈 따옴표인 경우 없다 취급 (길이가 0)
# s = null -> 오류가 난다.
s = "메롱" # length 가 1이상인 경우 True
if s:
    print("s는 값이 있다.")
else:
    print("s는 값이 없다.")

