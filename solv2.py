# we are going to create acronym generater
# Random Acces Memory =RAM
print("building a acronym generator")
i=input("enter the string for generating acronym ")
i=i.upper().strip() 
print(i)
k=i.split()
print(k)
s=""
for j in k:
    s=s+j[0]
print(i+"="+s)
    