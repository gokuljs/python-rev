print("program to reverese a string")
message=input("enter your string")
print(message)
print("revesrsed string is")
list=[]
list=message.split()
print(list)
n=len(list)
for i in range(n-1,-1,-1):
    print(list[i],end=" ")
