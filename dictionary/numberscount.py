words=[1,2,1,4,4,5,3,3,2]


numbers_count={}

for n in words:

    if n in numbers_count:

        numbers_count[n]+=1
    

    else:

        numbers_count[n]=1



print(numbers_count)
