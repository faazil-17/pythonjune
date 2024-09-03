#set

#==========


name={"hari","sukumar","hello","hello"}
# print(name)


#s=set()

#print(type(s))

#duplicates not allowed

#elements and unorderd

#cannot fetch a object using index position in set object

# mutable: we can add or remove the elements in the set


# >>>methods>>>


# name.add("kochi")  #to add an element to a set object

# print(name)

# name.clear()  #remove all elements from the set object

# print(name)

# name.pop()  #which remove a random elements from the set object

# print(name)

# name.discard("hello") #remove an element from the set if its a member in the object
# print(name)



# new_name=["hp","dell","lenovo"]


# name.update(new_name)  #add element from any collection to the set 

# print(name)


# set imp >>

# union()

# intersection()

# difference

new={"hey","hari","hlo"}

# new_set=name.union(new) #return the combined elements from the set and return as anew one

# print(new_set)



# intersected=name.intersection(new)  # retrun common elements from 2 set object as a new set

# print(intersected)


# differenced=name.difference(new) # return elements from the set names which is not in set new as a newset(differenced)

# print(differenced)


# symmetric=name.symmetric_difference(new) #combine all elements from 2 set and remove commen elements

# print(symmetric)