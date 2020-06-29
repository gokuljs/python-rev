# program to find permutation of the given string 
# in the length of the string is n then there is n! number of combination available
def tostring(a):
    return ''.join(a)
def permutation(a,l,r): #[a,b,c].0,2
    if(l==r):# 0!=2,
        print(tostring(a))
    for i in range(l,r+1): #0,3
        a[l],a[i]=a[i],a[l] #a[0],a[0]=a[0],a[0]
        print("a",a)
        print("l",l)
        print("r",r)
        permutation(a,l+1,r)# [a,b,c],1,4
        print("a",a)
        print("l",l)
        print("r",r)
        a[l],a[i]=a[i],a[l]

message=input("enter the string ") #abc
n=len(message) #a,b,c
print(n) #3
a=list(message) #[a,b,c]
print(a) 
permutation(a,0,n-1)
