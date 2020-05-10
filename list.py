import math
import random
# getting started with lists 
randomlist=["strings",3,5,6,7.877]
print(randomlist)
print("a list from a range of one to ten")
onetoten=list(range(10))
print(onetoten)
combinelist=randomlist+onetoten # combining two lists
print(combinelist)
print(combinelist[0])
print("getting list length")
print(len(combinelist))
print("getting first three items in the list")
neelist=combinelist[0:3]
print(neelist)
# cycling throught all the itme in the list 
for i in combinelist:
    print("{} : {}".format(combinelist.index(i),i))
print(combinelist[0] * 10)
combinelist.append("gokul")
print(combinelist.index("gokul")) # retuns the index value of the string 
print(combinelist.count("gokul")) # gives the number of occurences of the particular string got 
for i in combinelist:
    print("{} : {}".format(combinelist.index(i),i))
combinelist.append("hcscskhksd djjd")
for i in combinelist:
    print("{} : {}".format(combinelist.index(i),i))
