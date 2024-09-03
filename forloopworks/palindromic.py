num=int(input("enter the number :"))

orginal=num

sum=0

while(num!=0):

    digit=num%10

    sum=sum*10+digit

    num=num//10

print(sum)    


print(f"{orginal} is palindromic "if orginal==sum else f"{orginal} is not a palindromic")