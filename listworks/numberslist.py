numbers=[10,11,12,34,43,54,19,78,42]

print(len(numbers))

#print even numbers from this numbers

for i in range(0,len(numbers)):

    if numbers[i]%2==0:

        print(numbers[i])


#print total of numbers


total=0

for i in range(0,len(numbers)):

    total+=numbers[i]

print(total)


odd_total=0


for i in range(0,len(numbers)):

    if numbers[i]%2!=0:

      
        odd_total+=numbers[i]


print(odd_total)