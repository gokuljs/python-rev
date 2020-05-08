randomstring="     i am going to master python in one day      "
print(randomstring)
# going to remove white spaces in left side of the string 
print(randomstring.lstrip())
print(randomstring.rstrip())
print(randomstring.strip())
# cpatilizining the first letter in the string 
randomstring=randomstring.strip()
print(randomstring.capitalize())
print(randomstring.upper())
print(randomstring.lower())
# converting list into a string 
alist=["gokul","is","good","at","gaming"]
print(" ".join(alist))
# converting a list to string
alist2=randomstring.split()
print(alist2)
for i in alist2:
    print(i)
# going to find hw many times a string occurs in a string 
print("going to find hw many times a string occurs in a string ")
print(randomstring.count("python"))
# going to find a particular string inside a string 
print(randomstring.find("python"))# only going to return the index value
print(randomstring.replace("python","java"))