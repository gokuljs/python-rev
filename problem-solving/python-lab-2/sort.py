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

# len(list1)=4
# [1,3,4,2]
for i in range(0,len(list1)): # 0,1,2,3 = 1,3
    for j in range(i+1,len(list1)): # 1,2,3 ,3, 4
        if list1[i]>list1[j]: #a[1]>a[2]
            temp=list1[i] # temp=nothing,
            list1[i]=list1[j] #list1[i]=nothing,
            list1[j]=temp#list1[j]=nothing

print(list1)

#  or buy using built in method to solve a problem list1.sort()
