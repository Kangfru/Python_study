def multi_return():
    return 100, 200 # 튜플로 리턴됨 [100, 200] 의 형식일 시 리스트로 각각 리턴 가능

# main
a, b = 10, 20
print(a, b)

# 2개의 리턴값 2개의 변수에 각각 넣을 수 있다.
a, b = multi_return()
print(a, b)

c = multi_return()
print(c, type(c))

# 파라메터 값이 2개 또는 3개 등을 전달 받을 수 있는 함수 선언
def para_func(v1, v2, v3 = 0):
    return v1 + v2 + v3

print(para_func(10, 20))
print(para_func(10, 20, 30))