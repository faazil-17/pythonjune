word1="PQRS"

word2="ABCDEFG"



smallest_word=word1 if len(word1) < len(word2) else word2


merge_string=""


for i in range(0,len(smallest_word)):

    merge_string=merge_string+word1[i]+word2[i]

if len(word1)>len(word2):
    balance=word1[len(smallest_word):]

else:
    balance=word2[len(smallest_word):]


merge_string=merge_string+balance


print(merge_string)