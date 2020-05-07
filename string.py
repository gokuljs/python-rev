while True:
    try:
        number=int(input("enter the number"))
        break
    except ValueError: # 
        print("you didnt enter a number")
    except :
        print("an unknown error occured")

print("thanku for entering number")