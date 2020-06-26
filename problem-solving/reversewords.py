print("program to reverse the given words")
message=input("enter the string")
list=[]
list=message.split(" ")
print(len(list))
for i in range(len(list)-1,-1,-1):
    print(list[i],end=" ")
