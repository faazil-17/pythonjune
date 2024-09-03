f=open("C:\\Users\\fayiz\\OneDrive\\Desktop\\PythonJuneWorks\\FileOperations\\news.txt","r")

word_list=[w for line in f for w in line.rstrip("\n").split(" ")]

wc={w:word_list.count(w) for w in word_list}

print(wc)

def get_value(key):

    return wc.get(key)

srt=sorted(wc,key=get_value,reverse=True)

print(srt)