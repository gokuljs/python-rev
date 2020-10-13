def tostring(a):
    return ''.join(a)
def permutate(a,l,r):#(['a','b','c'],0,3-1)
    # l=0,1
    # r=2,2
    if l==r:#0!=2/1!=2
        print(tostring(a))
    else:
        for i in range(l,r+1):# 0,3/1,3
            a[l], a[i] = a[i], a[l] #a[0],a[0]=a[0],a[0]/a[1],
            permutate(a, l+1, r) #abc,1,2
            a[l], a[i] = a[i], a[l]
string=input("enter your string") #abc
n=len(string)#3
a=list(string)#['a','b','c']
print(a)
permutate(a,0,n-1)#(['a','b','c'],0,3-1)