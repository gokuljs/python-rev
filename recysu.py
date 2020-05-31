print("recusrsive program")
def fact(n):
    if(n<=1):
        return(1)
    else:
        return (n * fact(n-1))
i=int(input("enter your number"))
print(fact(i))