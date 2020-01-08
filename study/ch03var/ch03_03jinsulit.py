# 16진수의 FF를 10진수로 : 255
a = 0xFF
# 8진수의 77를 10진수로 :  63
b = 0o77
# 2진수 1111를 10진수로 : 15
c = 0b1111
print(a, b, c)

# 변수 a의 타입 출력
print("a의 타입은", type(a))

# 실수형 데이터 입력
a = 3.14
# e -> 지수형, e5 = 10의 5승을 뜻함
b = 3.14e5
print(a, b)
print("a의 타입은", type(a))

a = 10; b = 20
print(a+b)

a, b = 10, 20
print(a ** b)

b = 3
print(a / b)
print(a % b)
print(a // b)

a = True
b = False

print("a의 타입은", type(a))

a = 100 == 100
print(a)