list1=[1,2,3,4,53,32,3,12,322]
f=set(list1)
f.add(9)# adding new element into the set 
# want to add multiple values in the list 
list2=[2,2,2,5,534,232]
f.update(list2)
# removing an element in the set 
# print(f)
f.remove(2)# will show an error if elelment is present 
f.discard(32)# will not show an error if element is not present 
# print(f)

k=[1,2,3,4]
k=set(k)
l=[2,3,5,6,7,4]
l=set(l)
# f=k.intersection(l)
f=k.difference(l)
print(f)