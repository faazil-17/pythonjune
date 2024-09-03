numbers=[-3,5,7,1,9,2,0,10,4]


smallest_num=numbers[0]

second_smallest=numbers[-1]


for i in numbers:

    if i<second_smallest and i < smallest_num:

        second_smallest=smallest_num

        smallest_num=i


    elif i<second_smallest and i>smallest_num:

        second_smallest=i


print(second_smallest)