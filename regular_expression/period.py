
from re import findall


text="the the fat cat run very fast to catch rat"


pattern=".at"

matcher=findall(pattern,text)


print(matcher)


