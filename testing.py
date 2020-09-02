# birtday chocklate 
n=int(input("enetr the size of the chocklate"))
s=[int(ele) for ele in input().split()]
d,m=input().split()
d=int(d)
m=int(m)
count=0
# print(d)
for i in range(0,n-m+1):
    if sum(s[i:i+m])==d:
        count=count+1
print(count)
