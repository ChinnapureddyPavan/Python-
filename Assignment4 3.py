import string
txt=input("enter the string:")
res=all(letter in txt.lower() for letter in string.ascii_lowercase)
print(res)
