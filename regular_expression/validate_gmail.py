from re import fullmatch


gmail_id=input("enter the gmail:")



pattern="\\w[\\w\\._]*@gmail.com"


matcher=fullmatch(pattern,gmail_id)


print("invalid" if matcher==None else "valid")

# + match one or More

# ? optional

# * zero or more