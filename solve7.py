def sumall(*args):# this is passed if we dont know hw many argumenst are passed 
    sum=0
    for i in args:
        sum=sum+i
    return sum


print(sumall(1,2,3,3,4,4,4,5,5,6,6,6,78,8,8,8,9,9,0))