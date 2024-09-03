lst=[10,2,4,3,5,6]

# squares=[n**2 for n in lst]  #lst=[return ,iteration ,condition]

# cubes=[n**3  for n in lst]


# print(squares)

# print(cubes)


odd_numbers=[n for n in lst if n%2!=0]

print(odd_numbers)

even_numbers=[n for n in lst if n%2==0]

print(even_numbers)