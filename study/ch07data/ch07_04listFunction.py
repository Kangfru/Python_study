import copy

aa = [85, 100, 90, 70, 95, 90]

# 1. 리스트의 갯수를 출력
print("aa 리스트의 갯수 : ", len(aa))

# 2. 리스트의 데이터 바꾸지 않으면서 정렬해서 출력
print("aa 정렬 리스트 : ", sorted(aa))
print(aa)

# 3. 90데이터의 위치를 출력
print("aa 90의 위치 : ", aa.index(90))

# 4. 마지막 데이터를 꺼내면서 제거
aa.pop()
print("마지막 데이터 제거 : ", aa)

# 5. bb 라는 리스트에 동일한 데이터를 가지도록 처리
# 얕은 복사
bb = aa.copy()
print("복사한 bb : " , bb)
print(id(aa))
print(id(bb))

# 6. aa리스트에서 값이 100인 내용 지우기
del aa[aa.index(100)]
print("100을 삭제한 aa : ",aa)

# 7. aa리스트의 전체 내용 지운다
aa.clear()
print("전체 삭제 aa : ", aa)
