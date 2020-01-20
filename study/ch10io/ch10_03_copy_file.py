import os

# 입력 텍스트 파일 변수 선언
in_fp = None
out_fp = None

# 한 줄 단위 텍스트 읽은 데이터 저장
in_str = ""

in_fn = input("복사할 파일 입력 : ")

# 파일 명으로 존재하면 처리

if os.path.exists(in_fn):
    # 파일 읽기로 연결해서 사용
    # open(연결 파일명, 모드[r/w/+ 등])
    in_fp = open(in_fn, 'r', encoding = "UTF-8")
    out_fp = open("copy_" + in_fn, "w", encoding = "UTF-8")
    while True:
        in_str = in_fp.readline()
        if not in_str:
            print()
            print("복사가 완료되었습니다.")
            break
        out_fp.writelines(in_str)
        print(in_str, end = "")

    in_fp.close()
    out_fp.close()
    # 한 줄 단위로 읽어와 화면에 표시
else:
    # 파일이 존재하지 않는 경우
    print('파일이 존재하지 않습니다.')