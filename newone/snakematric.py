# idea is go row by row 
# if current row is even print from left to right 
# if current row is odd print from right to left
k=10
k=[[i+1 for i in range(5)]for j in range(5)]
print(k)
rows=len(k)
column=len(k[0])
for i in range(rows):
    if i%2==0:
        print(end="\n")

        for j in range(0,column):
            print(k[i][j],end=" ")
    else:
        print(end="\n")
        for j in range(column-1,-1,-1):
            print(k[i][j],end=" ")

        

        
