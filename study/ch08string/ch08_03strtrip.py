ss = " 파 이 썬 "
print(ss.strip())

def black_with_word(s):
    s = s.strip()
    while s.find("  ") >= 0:
        s = s.replace("  ", " ")
    return s

print(black_with_word(ss))
ss = " dddd         ddddddddddddd "
ss = "   파           이     썬    "

print(" ".join(ss.split()))