# 1. 수식을 작성하면 작성된 수식을 계산 후 출력
# 2. 숫자 2개를 입력받고 두 수 사이의 모든 숫자를 더한 후 출력.

# 변수 선언 부
select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

# 메인 코드
select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 모든 숫자 합"))

if select == 1:
    # 처리할 수식을 바는다.
    numStr = input("수식 입력 :")
    # 수식 처리
    answer = eval(numStr)
    print("%s 결과는 %5.1f" % (numStr, answer))

elif select == 2:
    # 시작 숫자 입력
    num1 = int(input("시작 숫자를 입력 : "))
    # 끝 숫자 입력
    num2 = int(input("마지막 숫자를 입력 : "))
    for i in range(num1, num2 + 1):
        answer += i
    print("%d 부터 %d 까지의 합 : %d" % (num1, num2, answer))

else:
    print("1 또는 2만 입력해주세요.")

