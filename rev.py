import random 
import sys
import os 


#simply printing the message
print("hello world");
# writting single line comment
'''
multiline comments 
'''
# in python u can store any type of variables 
name="gokuljs"
print(name);
value1=10
value2=1.5
print(value1);
print(value2);

# numbers , lists ,tuples, dictionary ,Strings 
# there are seven diffrent arithematic operaters 
# +,  -,  *,  /, % ,**(exponential calculations), // floor division
#Floor division is a normal division operation except that it returns the largest possible integer. This integer is either less than or equal to the normal division result. Floor function is mathematically denoted by this ⌊ ⌋ symbol.
print("=======================================================================")
print("5+2",5+2)
print("5-2",5-2)
print("5*2",5*2)
print("5/2",5/2)
print("5%2",5%2)
print("5//2",5//2)
print("5**2",5**2)

### order of operation 
'''
multiplication and division is going to happen fisrt then addition and subtraction

'''
print("=======================================================================")

quote="\" i am a better gamer" # if u want to add a quate inside a strign then this is the procedure to be followed 
print(quote);

## adding multiline string here 
multi_line_quote='''Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
     when an unknown printer took a galley of type and scrambled it to make a type specimen 
     book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''
print(multi_line_quote);


print("=======================================================================")

## if u dont need new line to work everytime
print("hello welcome to this new ",end="")
print("world")

## printing a newline character 
print(" \ngokul \n is a good a coading" * 5) # *5 is going to print this line 5 times in out put 



# getting started with lists 
grocery_list=['juice','fruits','vegetables','alcholal']
# list the count always starts from 0 goes still n-1 position
print("printing first item in the list",grocery_list[0])
# printing the subsets f the lists 
print(grocery_list[0:3])
# creating todolist 
todolist=['gaming','breakfast','coading']
print(todolist)
# combining to lists 
complete_list=[grocery_list,todolist]
print(complete_list) ## also an example for list inside an list 
## now there are twolists inside a list 
## now i want to use second item in the second list 
print(complete_list[1][0])
print(complete_list[1][2])
print(complete_list[0][3])
# appending items into the list 
grocery_list.append('oninons') ## normally this inserts value at the end of the list 
print(grocery_list)
## inserting value at very particular index in the list
##listname(indexvalue,"position you want to insert")
grocery_list.insert(1,"pickle")
print(grocery_list)
# removing item in the list then .remove
grocery_list.remove("pickle")
print(grocery_list)
# sorting item in the list 
grocery_list.sort();
print(grocery_list)
# reverse sorting the list 
grocery_list.reverse();
print(grocery_list)
# deleting an item
# del grocery_list
# print(grocery_list)
# deleteing specific item in list 
del grocery_list[4]
print(grocery_list)
todolist2=todolist+grocery_list
print(todolist2)
# getting lenght of the list 
print(len(todolist2))
# len id the built in function to get the string 
# getting maximum element in the list 
print(max(todolist2))
'''
The function is applied to each item on the iterable. If max() is called with an iterable, it returns the largest item in it. If the iterable is empty then the default value is returned, otherwise, a ValueError exception is raised. If max() is called with multiple arguments, it returns the largest one.Jan 7, 2020

'''
## getting minimum element in the list 
print(min(todolist2))


print("=======================================================================")
## getting started with tuples 

## tuples are simliar to list 
## but tuples cannot be changed once inserted 
## they use parthensis instead of square brackets 
# tuples can be converted to lists and viceversa

'''
Tuples are useful for representing what other languages often call records — 
some related information that belongs together, like your student record. ... So like 
strings, tuples are immutable. Once Python has created a tuple in memory, it cannot be 
changed.

'''
tuple2=(1,2,3,4,5,6,7,9)
print(tuple2)
# converting tuple into list 


list1=list(tuple2)
print(list1)
# converting list to tuple 
tuple1=tuple(list1)
print(tuple1)
print(len(tuple1))
print(min(tuple1))
print(max(tuple1))
print(tuple1[0])
print(tuple1[1:4])







