s="51Pa*0Lp*0e"
print(s)
n=len(s)
i=0
final=[None]*n
print(s)
s[0]=0
while(i<n-1):
    if i>=n:
        break
    elif ord(s[i])>=49 and ord(s[i])<=57:
        s[i]="0"
        i=i+1
    elif (ord(s[i])>=97 and ord(s[i])<=97+26) and (ord(s[i+1])>=67 and ord(s[i+1])<=67+26):
        swap(s[i],s[i+1])
        s[i]=chr(ord(s[i])+ord('a'))
        s[i+1]=chr(ord(s[i+1])+ord('a'))
        i=i+2
    else:
        i=i+1
print(s)
            
            
            