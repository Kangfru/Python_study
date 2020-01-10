# for 문을 이용해서
for i in range(1, 10):
    if i <= 5:
        for j in range(1, 6 - i):
            print(" ", end = "")
        for k in range(1, i*2):
            print("*", end = "")
        print("")
    else:
        for j in range(1, i-4):
            print(" ", end="")
        for k in range(1, (10 - i) * 2):
            print("*", end = "")
        print("")
