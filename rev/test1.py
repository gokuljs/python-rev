def tostring(a):
    return ''.join(a)
def permutate(a,l,r):
    if l==r:
        print(tostring(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l] 
            permutate(a, l+1, r) 
            a[l], a[i] = a[i], a[l]
string=input("enter your string")
n=len(string)
a=list(string)
print(a)
# print(permutate(a))
permutate(a,0,n-1)