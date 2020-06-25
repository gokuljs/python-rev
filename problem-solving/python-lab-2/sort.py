# // program to sort an array 
list1=[]
n=int(input("enter the number of elements u want to enter"));
for i in range(n):
    ele=int(input())
    list1.append(ele)
print("lenght =",len(list1))
print(n)
# print(list1[1]) [1,3,4,2]
# // process for sorting the array 
temp=0
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp

print(list1)
