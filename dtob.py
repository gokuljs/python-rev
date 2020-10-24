s="aaaaaaaaaabababsjsabsbgavsdauigsabsausajbsjabgsja"
n=len(s)
for i in range(n):
    for j in range(i+1,n+1):
        temp=[i:j]
        if temp==temp[::-1]:
            print(temp)