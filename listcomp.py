import random
import math
evenlist=[i*2 for i in range(10)]
# evenlist=[i*2(action we are going to perform) for i in range(10)]

print(evenlist)

numlist=[1,2,3,4,5]
#we are going to perform power of the all the element in the list
newlist=[math.trunc(math.pow(m,2)) for m in numlist]
print(newlist)
