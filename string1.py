print(type(3))
print(type(3.14))
print(type("gokul"))
print(type('k'))

samplestring="this is a very important string"
print(samplestring)
print(samplestring[0]) # positive value count starts from first 
print(samplestring[-1]) # negative value count starts from last
print(samplestring[3+7])
print("length =",len(samplestring))
print(samplestring[0:4])
print(samplestring[8:])
print("hello"+"world")
print("hello"*5)
num_string=str(4) 
print(type(num_string))
newstring="i am in to coading"
for char in newstring:
    print(char)
print("===================")
for char in range(0,len(newstring)-1,2):
    print(newstring[char])


# A-Z have unicodes from 65-90
# a-z 97-122
print("A=",ord("A")) # going to give the unicode of a 
print("65=",chr(65))
