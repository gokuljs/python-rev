import math

def rectangle():
    b=int(input("enter your breadth"))
    l=int(input("enter your length"))
    print(l*b)

def square():
    l=int(input("enter your length"))
    print(math.trunc(math.pow(l,2)))
def circle():
    r=int(input("enter the radius of the circle"))
    print(math.pi*math.pow(r,2))

def parallelogram():
    b=int(input("enter your breadth"))
    h=int(input("enter your height"))
    print(b*h)

def trapezoid():
    
    b1=int(input("enter your breadth one "))
    b2=int(input("enter your breath 2"))
    h=int(input("enter your height"))
    area=(h/2)*(b1+b2)
    print(area)





def get_area(shape):
    shape=shape.lower().strip()
    print(shape)
    if shape=="rectangle":
        rectangle()
    elif shape=="square":
        square()
    elif shape=="circle":
        circle()
    elif shape=="parrallelogram":
        parallelogram()
    elif shape=="trapezoid":
        trapezoid()
    else:
        print("invali")


def main():
    shape=input("get area for what shape ")
    get_area(shape)    






main()