# list는 데이터 변경이 가능 [], tuple타입은 데이터 변경 불가능 ()
tt = (10, 20, 30)

print(tt[0:2])
print(tt, type(tt))

# tt[2] = 300
# tt.append(40)
tt1 = tt

# tt1 = tt.copy() < - 없는 함수

print(tt + tt1)
print(tt * 3)

# tuple -> (10, 20, 30) --> (10, 200, 30)
# tuple -> list -> 데이터 수정 후 다시 -> tuple
aa = list(tt)
# aa[1] = 200
aa[aa.index(20)] = 200
tt = tuple(aa)
print(tt)