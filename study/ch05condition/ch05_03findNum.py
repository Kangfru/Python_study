import random

# random 으로 발생된 숫자 10개를 저장하는 list
numbers = []

# range(시작번호, 끝번호 + 1)
for num in range(0, 10):
    print("a", num + 1)
    # random.randrange(발생시작숫자, 끝숫자 + 1)
    numbers.append(random.randrange(0, 10))

print("생선된 리스트 : ", numbers)

# 0 ~ 9 사이 각각의 데이터가 있는 지 확인
for num in range(0, 10):
    if num in numbers:
        print('숫자 %d은(는) 리스트에 있습니다.' % num)
    if num not in numbers:
        print("숫자 %d은(는) 리스트에 없습니다." % num)

