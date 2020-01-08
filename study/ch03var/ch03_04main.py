# 함수 선언
def my_func():
    print("함수 호출")

#전역변수
gvar = 100

# 메인 코드
# if __name__ == '__main__':
# main 함수로만 선언을 한 경우 메인으로 인정을 못받음
# 함수 선언 없이 처리문을 만들거나 if __name__ 선언해서 처리
def main():
    print("메인 함수 부분")
    my_func()
    print("전역 변수 gvar : ", gvar)

#if __name__ == '__main__':
#   main()

# main 함수 호출로 간단히 구현 가능
main()
