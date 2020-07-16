# tail recursion is a type of recursion in which parent recursion has nothing to do when execution of child recursion finishes
#  tail recursions exceuted fast when there input size is large
#  main reason for the tailrecursion is fast because the caller dosent want to save the state
# tail recursion is one of the reason that quick sort is faster than merge sort 
#  for example finding a tail recursive problem using tail recursive method
def fact(n,k):
    if n==0 or n==1:
        print(k)
    fact(n-1,n*k)
n=int(input("enter your number for tail recursion"))
fact(n,1)

