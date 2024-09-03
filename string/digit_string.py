word="my name is fazil am 21 year old"

for ch in word:

    if ch.isalpha():
        print(ch,end="")


print("\n printing digits")


for ch in word:

    if ch.isdigit():
        print(ch,end=",")        



