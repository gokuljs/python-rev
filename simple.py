money=input("enter your money")
expected_intrest=input("enter your intrest")

money=float(money)
intrest=float(expected_intrest)*.01
for i in range (10):
    money=money+(money*intrest)

# print(3.345677*.01)

print("{:.2f}".format(money))