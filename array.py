import math
import random

array=[[0]*10 for i in range(10)]
print(len(array))

for i in range(len(array)):
    for j in range(len(array)):
        if(i==j):
             array[i][j]="{} : {}".format(i,j)
print(array)

for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j],end="||")
        print()

print(array)



