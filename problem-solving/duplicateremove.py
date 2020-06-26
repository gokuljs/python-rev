def remove(duplicate):
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list
print("program to remove duplicates from the string ")
message=input("enter the string so we can remove the duplicates")
list=[]
list=message.split(" ")
print(remove(list))
