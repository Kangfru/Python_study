foods = {"떡볶이": "오뎅",
         "짜장면": "단무지",
         "라면": "김치",
         "피자": "피클",
         "맥주": "소주",
         "치킨": "치킨무",
         "삼겹살": "상추"
         }

def main():
    while (True):
        my_food = input(str(list(foods.keys())) + " 중 좋아하는 음식은?")

        if my_food in foods:
            print("<%s> 궁합 음식은 <%s> 입니다. " % (my_food, foods.get(my_food)))

        elif my_food == "끝":
            break
        else:
            print("잘못 입력하셨습니다. 확인해보세요.")

main()