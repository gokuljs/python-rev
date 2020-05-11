arr=[1,4,5,6,7,9,82,3,4,45,6,6,7]

k=len(arr)
for i in range(k):
    for j in range(k-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

print(arr)