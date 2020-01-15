# 얕은 복사
old_list = ["짜장면"]
new_list = old_list
print("old_list : ", old_list)
print("new_list : ", new_list)

# 얕은 복사의 문제점 -> 단순 주소값 복사 -> 값이 같이 변형됨
old_list.append("탕수육")
print("old_list : ", old_list)
print("new_list : ", new_list)

new_list.append("깐풍기")
print("old_list : ", old_list)
print("new_list : ", new_list)

# 이를 방지 하기 위한 깊은 복사
old_list = ["짜장면"]
new_list = old_list.copy()
print("old_list : ", old_list)
print("new_list : ", new_list)

old_list.append("탕수육")
print("old_list : ", old_list)
print("new_list : ", new_list)

new_list.append("깐풍기")
print("old_list : ", old_list)
print("new_list : ", new_list)

print(id(old_list))
print(id(new_list))
