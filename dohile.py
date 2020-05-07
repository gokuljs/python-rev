# basic format of do while loop is too 
# code is executed onve then the condition is checked 
# do 
import random
i=True
while i:
    try:
        
        i =int(input("guess a number between 1 to 10"))
        x=random.randrange(1,10)
        if(i==x):
            print("guessed number is true ")
        else:
            print("gussed number is not true")

    except ValueError:
        print("please enter a number")

    except:
        i=False
        
        
        