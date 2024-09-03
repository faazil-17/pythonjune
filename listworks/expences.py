expences=[12000,13000,14000,15000,20000,35000,25000]



# expences_count=len(expences)


# print(expences_count)



# for i in range(0,expences_count):

    # print(expences[i])

# for i in range(0,len(expences)):

    # if expences[i]>15000:


        # print(expences[i])
total=0
for i in range(0,len(expences)):
    total=total+expences[i]

print(total)    

average_expence=total//len(expences)

print(average_expence)