print("program to remove duplicates from an array ")
list=[1,2,3,4,5,5,6,71,2,3,4,5]
list1=[]
n=len(list)
for i in range(n-1):
    # print("i = ",i)
    for j in range(i+1,n):
        # print("j =" ,j)
        if(list[i] not in list1):
            list1.append(list[i])
print(list1)            
        