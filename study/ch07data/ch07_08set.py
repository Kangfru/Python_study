# set : 중복된 데이터 배제 {v, v, v, ...}
my_set = {1, 2, 3, 3, 3, 4}
print(my_set)

sales_list = ['삼각김밥', '바나나', '도시락', '삼각김밥', '삼각김밥', '도시락', '삼각김밥']

print('삼각김밥 : ', sales_list.count('삼각김밥'))
print('바나나 : ', sales_list.count('바나나'))
print('도시락 : ', sales_list.count('도시락'))

for i in set(sales_list):
    print("%s 판매 : %d" % (i, sales_list.count(i)))

my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7}

# 교집합, 합집합, 차집합, 대칭차집합
print(my_set1 & my_set2)
print(my_set1 | my_set2)
print(my_set1 - my_set2)
print(my_set2 - my_set1)
print(my_set1 ^ my_set2)

print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))
print(my_set1.difference(my_set2))
print(my_set1.symmetric_difference(my_set2))

# 1~5 까지의 list를 만드시오
list1 = [1, 2, 3, 4, 5]
print("list1 : ", list1)

# 1~5 까지의 list for
list2 = []
for i in range(1, 6):
    list2.append(i)
print("list2 : ", list2)

# 컴프리헨션으로 리스트 만들기
list3 = [num for num in range(1, 6)]
print("list3 : ", list3)

# 1~10사이의 3의 배수로 리스트 만들기
# for i in range(1, 10 + 1):
#    if i % 3 == 0:
#        list2.append(i)
list4 = [num for num in range(1, 10) if num % 3 == 0]
print("list4 : ", list4)

# 1 ~ 5 사이의 데이터를 제곱근 구해서 리스트 만들기
list5 = [num * num for num in range(1,6)]
print("list5 : ", list5)

foods = ['떡볶이', '짜장면', '라면', '피자']
sides = ['오뎅', '단무지', '김치']

for food, side in zip(foods, sides):
    print(food, '-->', side)

end_point = len(sides) if (len(foods) > len(sides)) else (len(foods))

for i in range(0, end_point):
    print(foods[i], '-->', sides[i])

# zip 함수를 이용해서 튜플 리스트, 딕셔너리 만들기
tup_list = list(zip(foods, sides))
print(tup_list)
dic = dict(zip(foods, sides))
print(dic)