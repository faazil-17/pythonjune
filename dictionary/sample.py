# dict ={key:value}

#student={"name":"sukumar","course":"fullstack"} #//if dictionary key should be unique

# <class dict> : collection of elements as a key : value pairs

# print(student["name"])

# print(student["course"]) 

# student["name"]="hari"

# print(student)

#student["name"]="hari"

#student["place"]="chennai"  # overwrites the value if the key is present else add as a  new pair 

# print(student)



#new=student.items() # dict_item (['name','hari'),('course','fullstack'),('place','chennai')])

#print(new)


# student={"name":"sukumar","course":"datascience"}


# for i in student:

#     print(f"{i} =  {student[i]}")

# update the course as fullstack in students in iteration



# student={"name":"sukumar","course":"datascience"}


# for i in student:

#     if i =="course":

#         student[i]="fullstack"


# print(student)


#delete a key "place" if it present in the dict using iteration

student={"name":"sukumar","course":"datascience","place":"kannur"}


for i in student:

    if i=="place":


        new=student.pop       







