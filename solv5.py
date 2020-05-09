def isprime(a):
    for i in range(2,a):
        if(a%i==0):
            return False
        else:
            return True

def isrange(a):
    for i in range (2,a):
        if(isprime(i)):
            print(i)

i=int(input("enter your number for "))
isrange(i)




