import turtle
import random


# 함수 선언
# 왼쪽 마우스 클릭 - 선을 그린다.
def screen_left_click(x, y):
    global r, g, b
    # 포함관계는 {}를 사용하지 않고 들여쓰기를 ㅏㄴ다.
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)


# 오른쪽 마우스 클릭 - 이동만 -> 그리지 않는다.
def screen_right_click(x, y):
    turtle.penup()
    turtle.goto(x, y)


# 마우스 가운데 버튼 색상과 거북이 크기 조정
def screen_mid_click(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()


pSize = 10
r, g, b = 0.0, 0.0, 0.0

turtle.title("거북이로 그림 그리기")
turtle.shape("turtle")
turtle.pensize(pSize)

# 클릭 이벤트 처리
# 왼쪽 버튼 클릭 이벤트( , 1)
# 왼쪽 마우스 클릭 - 선을 그린다.
turtle.onscreenclick(screen_left_click, 1)
# 가운데 버튼 클릭 이벤트( , 2)
turtle.onscreenclick(screen_mid_click, 2)
# 오른쪽 버튼 클릭 이벤트( , 3)
turtle.onscreenclick(screen_right_click, 3)


# 실행된 창을 유지
turtle.done()