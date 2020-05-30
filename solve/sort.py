print("sorting an array ")
n=int(input("enter total number of elements you want to sort"));
list1=[]
for i in range(n):
    k=int(input("enter your elements"))
    list1.append(k)
print("all the elements before sorting")
print(list1)
min=0
max=0
# # 1 2 3 4 7 89 
# for i in range(n):
#     for j in range(i+1,n):
#         if list1[i]>list1[j]:
#             max=list1[i]
#             min=list1[j]
#             list1[i]=min
#             list1[j]=max

# print(list1)
list1.sort()
print(list1)
