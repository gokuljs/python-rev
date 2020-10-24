# k=[[0 for i in range(13)]for j in range(10)]
k=[[0 for i in range(2)]for j in range(3)]
for i in range(3):
    for j in range(2):
        s=10
        k[i][j]=s
print(k)
print(len(k))
print(len(k[0]))
for i in range(3):
    for j in range(2):
        print(k[i][j])