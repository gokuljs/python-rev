# solve for x
# X+4=9

def solve(name):
    x , add, num1, equal, num2=name.split()
    num1, num2=int(num1),int(num2)
    print("X = "+str(num2-num1))
name=input("enter your algebric equation ")
name=name.strip()
solve(name)