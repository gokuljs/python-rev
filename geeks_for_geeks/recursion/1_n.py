def rec(n):
    if n==0:
        return
    rec(n-1)
    print(n)
    
    
n=int(input("enter your python"))
rec(n)