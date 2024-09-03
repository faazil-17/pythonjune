
from json import load


f=open("C:\\Users\\fayiz\\OneDrive\\Desktop\\PythonJuneWorks\\jsonworks\\flims.json")


flims=load(f)

for fl in flims:

    print(fl.get("title"))