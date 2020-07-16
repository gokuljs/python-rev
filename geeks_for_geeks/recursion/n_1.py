def rec(n):
    if n==0:
        return
    print(n)
    n=n-1
    rec(n)
n=int(input("enter the value"))
rec(n)