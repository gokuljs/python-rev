# program to reverse an array without another array 
n=int(input("enter the number of elements"))
list=[]
for i in range(n):
    ele=int(input())
    list.append(ele)
print("array before sorting")
for i in range(n):
    print(list[i])
# 1,2,3,4,5,6,7
reversed_list=[]
print("reversed array is ")
for i in range(n-1,-1,-1):
    print(list[i])
    reversed_list.append(list[i])
print(reversed_list)