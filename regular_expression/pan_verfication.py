# validte pancard number

# first 3 character are alphabets

# 4th place PCAFHT

# 5th place alphabet

# 4 digit

# 1 alphabet



from re import fullmatch


text=input("enter pan number:")


pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"


matcher=fullmatch(pattern,text)


print("invalid" if matcher==None else "valid")