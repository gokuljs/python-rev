for i in range(10):
    print(i)


for i in range(10):
    if(i%2==0):
        print(i,"even")
    else:
        print(i,"odd")

# workign with floating point number 
num=input("enter your number in floating point")
num2=float(num);
print("roubd to two decimal places : {:.2f}".format(num2))
print("round for three decimal places :{:.3f}".format(num2))

