# getting started with getters and setters
class Rectangle:
    def __init__(self,height=0,width=0):
        self.height=height
        self.width=width

    def run(self):
        area=self.height*self.width
        return area

def main():
    height=int(input("enter the the length of the recatngle "))
    width=int(input("enter the width of the rectangle "))
    area1=Rectangle(height,width)
    rectanglearea=area1.run()
    print(rectanglearea)
    






main()