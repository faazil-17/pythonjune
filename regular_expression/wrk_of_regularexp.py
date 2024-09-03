
from re import finditer


text="addadcassaddcdaadd"


match_add=finditer("add",text)

count=0

for m in match_add:


    print(m.start(),"==",m.group())

    count+=1

print("count==",count)

