text="racecar"


longest_paidrome=""


for i in range(0,len(text)):

    left=i


    right=i


    while(left>=0  and right<len(text) and text[left]== text[right]):

        current_palidrome=text[left:right+1]

        if len(current_palidrome) > len(longest_paidrome):

            longest_paidrome=current_palidrome

        left=left-1 

        right=right+1 



print(longest_paidrome)          

