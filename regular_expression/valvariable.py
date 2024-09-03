
from  re import fullmatch


text=input("enter the var=")



pattern="[k-m][369][a-zA-Z0-9@]*"



matcher=fullmatch(pattern,text)


print("invalid" if matcher==None else "valid")