import random
import math

#creating a multiplication table 
tablelist=[[0]*10 for i in range(10)]
print(tablelist)
print(len(tablelist))
for i in range(len(tablelist)):
    for j in range(len(tablelist)):
        tablelist[i][j]=(i+1)*(j+1)

for i in range(len(tablelist)):
    for j in range(len(tablelist)):
        print(tablelist[i][j],end=" ")
    print()