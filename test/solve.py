string=input("enter your string ")
string=string.lower()
list=['a','e','i','o','u']
consonant=0
vowel=0
for i in string:
    if i in list:
        consonant=consonant+1
    else:
        vowel=vowel+1
print(consonant)
print(vowel)

        