import random

lotto = []
lottoSet = set()
num = 0

print("로또 추첨")

def getLotto():
    while len(lotto) < 6:
        num = random.randrange(1, 46)
        if num in lotto:
            continue
        else:
            lotto.append(num)

print("추첨된 로또번호 --> ", end = "")
getLotto()
lotto.sort()
for i in range(0, 6):
    print("%d " % lotto[i], end = "")


def getSetLotto():
    while len(lottoSet) < 6:
        lottoSet.add(random.randrange(1, 46))

print()
getSetLotto()
print(sorted(lottoSet))