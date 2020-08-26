# reverse in group s
# arr=[1,2,3,4,5,6,7,8,9,10,11,12]
arr=[1,2,3,4,5]
n=len(arr)
k=3
s=-1
list=[]
i=0
while i<n:
    if k<n:
        for j in range(k-1,s,-1):
            list.append(arr[j])
        s=k-1
        k=k+k
    i=k
if len(list) != n:
    for i in range(len(list),n):
        list.append(arr[i])
        
print(list)