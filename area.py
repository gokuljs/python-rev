import math

def rectangle():
    b=int(input("enter your breadth"))
    l=int(input("enter your length"))
    print(l*b)

def square():
    l=int(input("enter your length"))
    print(math.trunc(math.pow(l,2)))


def get_area(shape):
    shape=shape.lower().strip()
    print(shape)
    if shape=="rectangle":
        rectangle()
    elif shape=="square":
        square()
    else:
        print("invali")


def main():
    shape=input("get area for what shape")
    get_area(shape)    






main()