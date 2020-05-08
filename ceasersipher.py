# ceaser cipher 
# working 
# consider if we type a it will be shifted by 3 d if b then it will be E
# A-Z to 65-90
# a-z to 97-122
print("wap for ceaser cipher")
print("encryption part")
message=input("enter your string ")
key=int(input("enter your shift value "))
secret=""
for char in message:
    if (char.isalpha()):
        code=ord(char)
        print(code)
        code=code+key
        if(char.isupper()):
            if(code>ord('Z')):
                code=code-26
            elif(code<ord('A')):
                code=code+26
        if(char.islower()):
            if(code>ord('z')):
                code=code-26
            elif(code<ord('a')):
                code=code+26
        secret=secret+chr(code)
print("decrytption part")
originalmessage=""
for k in secret:
    if (k.isalpha()):
        decrypt=ord(k)
        decrypt=decrypt-key
        # print(chr(decrypt))
        originalmessage+=chr(decrypt)
print("secret message generated is ",secret)        

print("original message =",originalmessage)



    


