#dictionaries 
gokul={
    "fname":"gokul js",
    "age":"19",
    "laname":"great",
}

print(gokul)
print(gokul["fname"])
gokul["lanme"]="js"
print(gokul)
gokul["city"]="banglore"
print(gokul)
print("city" in gokul)
print(gokul.values())
print(gokul.keys())

for k,v in gokul.items():
    print(k,v)

print(gokul.get("mname","not here"))# if mname is not present in dictionary then it will return not here 

for i in gokul:
    print(i)

# clearing all the data inside dict 
gokul.clear()

# creating dict inside list