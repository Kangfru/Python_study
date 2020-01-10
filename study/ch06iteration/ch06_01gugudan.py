# 구구단 처리를 하는데 시작 단수와 마지막 단수를 입력 받아서 시작 단수부터 마지막 단수 사이의 모든 단수를 출력한다.
# 단 1줄에 시작단수 ~ 마지막단수

start = int(input('시작 단수를 입력하세요'))
end = int(input('마지막 단수를 입력하세요'))

for i in range(start, end + 1):
    print("   -%d 단-  " % i, end = "")
print()

for i in range(1, 10):
    for j in range (start, end + 1):
        print("%d * %d = %2d" %(j, i, i*j), end = " ")
    print()