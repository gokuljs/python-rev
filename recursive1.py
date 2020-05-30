fname={
    "fname":"gokul",
    "lanme":"js",
    "address":"welocomre to my house",
    }
fname["address"]="get out of my house"
fname["city"]="banglore"
print(fname["address"])
print("is there a city","city" in fname)
print(fname.values()) # getting list of values
print(fname.keys()) # getting list of keys 
for k,v in fname.items():
    print(k+" = " +v)
print(fname.get("lanme"))
print(fname)


del fname["city"]
print(fname)

for i in fname:
    print(i)

# clearing all the elements inside the lists
fname.clear();

employees=[]
fname,lname=input("enter employee name : ").split()
employees.append({
        'fname':fname,
        'lname':lname,
});
print(employees)