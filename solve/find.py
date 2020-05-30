print("python program to print a string until an input letter is found ")
message=input("enter the a simple string ")
print(message)
letter=input("enter your letter in ")
l=len(message)
for i in range(l):
    if letter==message[i]:
        break
    else:
        print(message[i],end="")