# converting binary to decimal number 
k=int(input("enter the decimal number"))
rev=0
i=0
# //cyclic rotation of binary numbers 

while(k>0):
    dig=k%10
    rev=rev+dig*pow(2,i)
    k=k//10
    i=i+1
j=0

maxnum=0
while(1):
    if pow(2,j)>rev:
        break 
    if rev%pow(2,j)==0:
        print(rev%pow(2,j),"for",j)
        maxnum=max(maxnum,j)
        print(maxnum)
    j=j+1
print("========")
print(rev)
print(maxnum)


