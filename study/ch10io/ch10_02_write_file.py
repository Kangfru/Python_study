import os

# 출력 파일 객체 선언
outfp = None

# 출력할 파일명 입력
outfn = input("출력할 파일명 입력:")

# 파일 객체를 쓰기로 열기
outfp = open(outfn, "w")

instr = ""

# 글자를 입력하대로 출력하기를 한다.
while True:
    instr = input("텍스트 입력:")
    # 빠져나갈 조건 -> 입력을 안하고 엔터 누른다.
    if not instr:
        break
    outfp.writelines(instr)

outfp.close()

