price=[100,80,60,70,60,75,85]
span=[]
span.append(1)
count=1
n=len(price)
for i in range(1,n):
    for j in range(i-1,-1,-1):
        if price[i]>price[j]:
            count=count+1
        elif(price[i]<price[j]):
            count=count
            break
    span.append(count)
    count=1
print(span)

