f_read=open("C:\\Users\\fayiz\\OneDrive\\Desktop\\PythonJuneWorks\\FileOperations\\century.txt","r")
f_centuary=open("C:\\Users\\fayiz\\OneDrive\\Desktop\\PythonJuneWorks\\FileOperations\\century.txt","w")
f_noncentuary=open("C:\\Users\\fayiz\\OneDrive\\Desktop\\PythonJuneWorks\\FileOperations\\noncentury.txt","w")

for year in f_read:

    y=int(year.rstrip("\n"))

    if y%100==0:

        f_centuary.write(str(y)+"\n")

    else:

        f_noncentuary.write(str(y)+"\n")