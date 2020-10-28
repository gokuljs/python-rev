arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16 ]]
row=len(arr)
col=len(arr[0])
if row==0:
    for i in range(0,col):
        print(arr[0][i])
elif col==1:
    for i in range(row):
        print(col[i][0])
else:
    for i in range(col):
        print(arr[0][i],end="")
    print(end="\n")
    for i in range(row):
        print(arr[i][0],end="") 
