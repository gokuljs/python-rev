i="z"
j="3"
space=" "
k="3.122"

def isfloat(a):
    try:
        float(a)
        # print("aaa")
        return True
    except ValueError:
        return False
    

print(i.isalnum())
print(i.isalpha())
print(j.isdigit())
print(i.isdigit())
print(i.isupper())
print(i.islower())
print(space.isspace())
print("===")
print(isfloat(k))
print(isfloat(space))



