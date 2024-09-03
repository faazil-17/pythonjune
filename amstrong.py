num=int(input("enter number:"))

orginal=num

sum=0

digit_count=len(str(num))

while(num!=0):
    digit=num%10

    exponent=digit**digit_count
    
    sum=sum+exponent
    
    num=num//10


print(f"{orginal} is amstrong "if orginal==sum else f"{orginal} is not a amstrong")
   