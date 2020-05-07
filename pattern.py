# bulding a pattern 
# use 1 while loop and 3 for loops
# 4 spaces : 1 hashes 
# 3 spaces : 3 hashes 
# 2 spaces : 5 hashes 
# 1 spaces : 7 hashes 
# 0 spaces : 9 hashes 

# need to do

print("enter the tree height you want to print ")
i=int(input("enter the value"))
tree_height=i
spaces=tree_height-1
hashes=1
stumpspaces=tree_height-1
print(tree_height)
print(spaces)


while(tree_height!=0):
    for i in range(spaces):
        print(" ",end="")
    for i in range(hashes):
        print("#",end="")
    print("\n")
    spaces=spaces-1
    hashes=hashes+2
    tree_height=tree_height-1

for i in range(stumpspaces):
    print(' ',end="")
print("#")






