i=input("enter your string in upper case letters = ")
# orginalmessage=i
s=""
k=""
for char in i:
    s=s+str(ord(char))
    # print(s)
print("secretmessage = ",s)
o=""
for k in range(0, len(s)-1 , 2): 
    # k=0 0,1
    # k=2 2,3

    # print(k)
    value=s[k]+s[k+1]
    # print(value)
    o=o+chr(int(value))

    # # o=o+chr(int(value))
    # print(o)
print("original message =",o)

    