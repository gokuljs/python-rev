import os 

with open("file.txt",mode="w",encoding="utf-8") as myfile:
    myfile.write("some random text \n more random text \n even more random text\n welcome to random text")

with open("file.txt",mode="r",encoding="etf-8") as myfile:
    linenum=1
    line=myfile.readline()
    if not line:
        break
    print("line",linenum)



    linenum=+1
