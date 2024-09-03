from re import fullmatch

text=input("enter mnth:")


pattern="(0?[1-9]|1[0-2])"


matcher=fullmatch(pattern,text)

print("invalid" if matcher==None else "valid")