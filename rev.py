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

