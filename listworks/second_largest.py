numbers=[13,2,5,7,1,11,10]


# numbers.sort()


# print(numbers[-2])

# with out method


largest_num=0

second_largest=0


for i in numbers:


    if i > second_largest and i > largest_num:


        second_largest=largest_num


        largest_num=i

    elif i > second_largest and i < largest_num:

        second_largest=i

print(f"second largest is {second_largest}")