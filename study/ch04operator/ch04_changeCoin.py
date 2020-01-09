def exchangeCoin(money):
    result = [0, 0, 0, 0]
    result[0] = money // 500
    money %= 500
    result[1] = money // 100
    money %= 100
    result[2] = money // 50
    money %= 50
    result[3] = money // 10
    money %= 10
    print (result, money)


def main():
    money = int(input("교환할 돈은 얼마?"))
    exchangeCoin(money)


main()