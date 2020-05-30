print("proggram to reverse an array without using another array")
# n=int(input("enter the length of an array"))
list=[1,2,3,4,5,6,7,8,9]
n=len(list)
# for i in range(n):
#     # k=int(input("enter your element "))
#     list.append(k)
# for i in range(n-1,-1,-1):
    # print()
    # print(i," ",list[i])
start=0
end=len(list)-1
k=0
while(start<end):
    list[start],list[end]=list[end],list[start]
    start=start+1
    end=end-1

print(list)
