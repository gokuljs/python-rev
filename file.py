import os 
with open("file.txt",mode="w",encoding="utf-8") as myfile:
    myfile.write("some randome text \n more randome text \n ur going to be random as fuck ")

with open("file.txt",mode="r",encoding="utf-8") as myfile:
    # print(myfile.read()) # going to read everything 
    # print(myfile.readlines())
    print(myfile.readline()) # only going to read ine line  untill i find a new line a charatcer
print(myfile.closed)
print(myfile.name)
# renaming the file name using os package
# os.rename("file.txt","file1.txt")
# remiving files inside  operating system
os.remove("file.txt")
# creating new directories 
# os.mkdir("new")
# os.mkdir("welcome")
# changeing into new directory that was created 
os.chdir("new")
print("now printing the current directory is",os.getcwd())
os.chdir("..")
# coming one step backwords from the current directory 
print("now printing the current directory is",os.getcwd())
# removing a directory 
os.rmdir("new")
