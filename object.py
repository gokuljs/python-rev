# real world objects
#  the have attributes and capabilities 
#  for example 
#  example dog have attributes like height,weight,favourite food
# in object oriented programming attributes are called fields which are called has variables and capabilities are called has methods also knows as function 
# examples for capabilites is run, walk ,eat 


class dog:
    #  class is a template which is used to create objects 
    def __init__(self,name="",height=0,weight=0):
        #  normally when u create a dog u will intialize its name etc inside init method
        # self just allows an object to refer to itself like my height etc
        self.name=name
        self.height=height
        self.weight=weight

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats ".format(self.name))
    
    def bark(self):
        print("{} the dog barks ".format(self.name))


def main():
    spot=dog("spokke",24,30)
    spot.bark()
    spot.eat()

    bowser=dog()
    bowser.bark()


main()