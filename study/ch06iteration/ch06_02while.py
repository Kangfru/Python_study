# 1 ~ 10까지 출력

i = 1
while i < 11:
    print(i)
    i += 1

# 1부터 숫자를 계속 더해서 더한 숫자가 100보다 커지면 빠져나가 출력
i = 1
sum = 0
while True:
    sum += i
    i += 1
    if sum > 100:
        break

print(i, sum)

# 1 ~ 10 출력 홀수만 출력
# 1부터 시작하면서 2씩 증가, -> 첫번째 방법


# 짝수인 경우 출력하지 않고 반복처리
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)