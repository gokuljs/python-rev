list1=[1,2,3,4,53,32,3,12,322]
f=set(list1)
f.add(9)# adding new element into the set 
# want to add multiple values in the list 
list2=[2,2,2,5,534,232]
f.update(list2)
# removing an element in the set 
print(f)
f.remove(2)
f.discard(32)
print(f)