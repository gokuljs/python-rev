# 1, 1, 2 ,3 ,5

def fib(n): #2,3 

    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        print(fib(n-1))
        print(fib(n-2))
        print("-======33")
        result=fib(n-1)+fib(n-2) #2-1 +2-2 =1+0, 1+1=2
        return result

i=int(input("enter your number for fibonnaci numbers"))
print(fib(i))



