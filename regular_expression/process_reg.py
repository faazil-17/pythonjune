

from re import fullmatch


f=open("C:\\Users\\fayiz\\OneDrive\\Desktop\\PythonJuneWorks\\regular_expression\\regnumbers.txt")


pattern="(KL)( )?[0-9]{2}( )?[A-Z]{1,2}( )?[0-9]{4}"

for line in f:



    vehicle_num=line.rstrip("\n")
    
    
    matcher=fullmatch(pattern,vehicle_num)


    if matcher !=None:

        print(vehicle_num)

