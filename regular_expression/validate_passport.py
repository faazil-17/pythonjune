from re import fullmatch



passport=input("enter number:")


pattern="[A-Z][1-9][0-9][0| ][0-9]{4}[1-9]"


matcher=fullmatch(pattern,passport)


print("invalid" if matcher==None else "valid")

