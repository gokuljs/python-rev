import os
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        result=fib(n-1)+fib(n-2)
        return result
print("program to print fibonnaci for series of numbers ")
i=int(input("enter your numbers"))
with open("fib.txt",mode="w",encoding="utf-8") as myfile:
    for k in range(i):
        myfile.write(str(fib(k)))
        
    

