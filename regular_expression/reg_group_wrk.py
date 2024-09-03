
from re import finditer


text="abc123 @K#7LMdef"


# pattern="[abf]" #chk for either a b or f

# pattern="[a-k]"#chk for alphabets from a to  k

# pattern="[a-z]"#chk for all alphabets

# pattern="[A-Z]" #chk for all uppercase alphabets

# pattern="[A-Za-z]" #chk for all matching alphabets

# pattern="[0-9]" #chk for all digits


# pattern="[A-Za-z0-9]" #chk for all alphanum characters

# pattern="[^0-9]" #chk not num char

# pattern="[^A-Za-z0-9]" #chk for all special char and space


# pattern="[\s]" #chk for space



pattern="[^A-Za-z0-9\s]" #chk for all special char






matcher=finditer(pattern,text)


for m in matcher:

    print(m.start(),"==",m.group())