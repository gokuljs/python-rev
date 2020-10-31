arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
row=len(arr)
col=len(arr[0])
temp=[[0 for i in range(col)]for j in range(row)]
print(temp)
for i in range(row):
    for j in range(col):
        temp[col-j-1][i]=arr[i][j]
print(arr)
print(temp)

