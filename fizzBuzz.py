# read a number from user
#  print fizz if num is /by 3
# print buzz if num is / by 5
# print fizzbuzz if num is / by 15

num=int(input(f"enter a number :>>"))


if num%15==0:
    print(f"{num} is  fizzbuzz") 



elif num%5==0:
    print(f"{num} is  buzz")     


if num%3==0:
    print(f"{num} is  fizz") 


else:
    print("invaild") 

