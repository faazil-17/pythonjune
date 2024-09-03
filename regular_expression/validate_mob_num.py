# validate mobile number with country code mandatory

from re import fullmatch


mob_num=input("enter mob num:")



pattern="(91)\\s?[6-9][0-9]{9}"


matcher=fullmatch(pattern,mob_num)


print("invalid" if matcher==None else "valid")


