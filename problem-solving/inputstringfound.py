# prgrom  to find that entered string is found in given string or not
message=input("enter the message ")
input_string=input("enter the substring u want to find in the main string ")
list=[]
list=message.split(" ")
print(list)
# print(message)
for i in range (0,len(list)):
    if list[i]== input_string:
        break
    else:
        print(list[i],end=" ")
