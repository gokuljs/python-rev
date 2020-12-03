arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
row=len(arr)
col=len(arr[0])
temp=[[0 for i in range(col)]for j in range(row)]
for i in range(row):
    for j  in range(col):
        temp[i][j]=arr[j][i]
print(temp)
text=0

for i in range(col):
    low=0
    high=row-1
    while(low<high):
        text=temp[low][i]
        temp[low][i]=temp[high][i]
        temp[high][i]=text
        low=low+1
        high=high-1
print(arr)
print(temp)

# print(temp)
# for i in range(row):
#     for j in range(col):
#         print(i,"=",col-j-1)
#         temp[col-j-1][i]=arr[i][j]
# print(arr)
# print(temp)



