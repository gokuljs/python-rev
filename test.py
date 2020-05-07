import random 

x=random.randrange(1,100);
print(x)

for i in range (100):
    x=random.randint(1,1000);
    print(x)

# if ur using the random module and then never name ur file random.py
i=1
while i<=20:
    if(i%2==0):
        i+=1
        continue# so wat constinue does is if statement is true it will leave rest of the while body and again start from starting 
    if(i==15):
        break # break is used to come out the loop