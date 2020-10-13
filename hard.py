# making anagrams 
from collections import Counter
s="abc"
s1="cde"
a=Counter(s)
b=Counter(s1)
print(a-b)
print(a)
print(b)