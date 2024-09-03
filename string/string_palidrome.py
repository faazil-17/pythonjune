# create a function is_palidrome(word) return True if word is a palidromic string
# else return False


def is_palidrome(word):

    reversed_str=word[::-1]
    
    
    return word==reversed_str


print(is_palidrome("wow"))

