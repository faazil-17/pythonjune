num=int(input(f"enter the number:"))


previous=0

current=1

isfib=False

next=1  #next=previous+current



while(next<=num):

    next=previous+current

    previous=current

    current=next



    if(next==num):
        
        isfib=True


        break

print(f"{num} is fibnacci" if isfib==True else f"{num} is not fibnacci " )


