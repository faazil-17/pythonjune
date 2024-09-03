arr=[10,11,12,13,14,15,16,17]

left=1

lenght=len(arr)-1

if lenght%2!=0:

    right=lenght

else:
    
    right=lenght-1


while(left<right):


    (arr[left],arr[right])=(arr[right],arr[left])

    left=left+2


    right=right-2


print(arr)