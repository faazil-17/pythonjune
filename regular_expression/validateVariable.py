from re import fullmatch


text=input("enter the variable=")


pattern="[a-zA-Z][a-zA-Z0-9_]*"



matcher=fullmatch(pattern,text)


print("invalid" if matcher==None  else "valid")