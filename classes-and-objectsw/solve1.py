# real world objects have attributes and capabilities
# for example dog has attributes(which are also called fileds) like height,weight,fovourite food
# dog also have capabilities(which are also called functions or methods we can say  ) like run,walk,eat

class Dog:
    # when ever u try to create class there are propabaly some values u want to set 
    # this all are done in init method
    def __init__(self,name="",height=0,weight=0):
        # self allows an object toitself ,just like u would refer to yourself as my like 
        # my height,my weight self is exactly the same has that
        self.name=name
        self.height=height
        self.weight=weight

    def run(self):
        print("{} the dog runs".format(self.name)) 

    def eat(self):
        print("{} the dog eats".format(self.name)) 

    def bark(self):
        print("{} the dog barks".format(self.name)) 

def main():# this is where all our execution starts
    # creating a new dog object
    spot=Dog("randy",26,56)
    spot.bark()
    bowser=Dog()
    bowser.bark()




main()