customer=[]
while(1):
    createentery=input("enter your customer Yes/No :")
    createentery=createentery[0].lower()
    if createentery == 'n':
        break
    else:
        fname,lname=input("enter your name ").split()
        customer.append({
            "fname":fname,
            "lname":lname,
        })

for cust in customer:
    print(cust["fname"])
    print(cust["lname"])
    print("===========================")