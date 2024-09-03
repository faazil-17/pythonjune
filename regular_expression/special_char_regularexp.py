from re import finditer


text="abc 7Klefg@#"


# pattern=r"\d" #"[0-9]"     !! r"\d"=="\\r"==(regularexp)!!

# pattern=r"\D" #"[^0-9]"

# pattern=r"\w"  #[a-zA-Z0-9]


# pattern=r"\W"  #specail chr and space

# pattern=r"\s"  #space


pattern=r"\S"  #excluded space



matcher=finditer(pattern,text)


for m in matcher:


    print(m.start(),"==",m.group())