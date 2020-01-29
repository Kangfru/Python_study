#파이썬에서 액셀 다루는 라이브러리
import openpyxl

filename = "stat_104101.xlsx"
#액셀 불러오기
book = openpyxl.load_workbook(filename)
# 첫번째 워크시트 불러 오기
sheet = book.worksheets[0]

data = []
# 데이터값 리스트로 변경 0이랑 9만 받기
for row in sheet.rows:
    data.append([
     row[0].value,
     row[9].value

    ]
    )
#0부터 2까지 인덱스 지우기
del data[0:3]

print(data)
# 1번 값으로 정렬
data = sorted(data, key = lambda x:x[1])

# i는 0부터 시작하는 순서 번호 a 는  데이터값
for i, a in enumerate(data):
    if (i >=5): break
    print(i+1, a[0], int(a[1]))

#활성화 된 시트 가져오기
sheet = book.active

for i in range(0,9):
    # b3에 벨류값을 정수형으로 바구기
    total = int(sheet[str(chr(i+66))+"3"].value)

    # b4에 벨류값을 정수형으로 바구기
    seoul = int(sheet[str(chr(i+66))+ "4"].value)
    # 아웃풋 은토탈 빼기 서울
    output = total - seoul
    print("서울 제외 인구 =",output)
    # b 21 에 아웃풋 데이터 추가
    sheet[str(chr(i+66))+"21"] = output
    # b21을 셀에 저장
    cell = sheet[str(chr(i+66))+"21"]
    # 셀 서식 변경
    cell.font = openpyxl.styles.Font(size=14,color="FF0000")
    cell.number_format = cell.number_format
#이름 설정
filename="population.xlsx"
#엑셀 저장
book.save(filename)
print("ok")