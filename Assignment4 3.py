import string
txt=input("enter the string:")
res=all(letter in txt.lower() for letter in string.ascii_lowercase)
if res: 
    print("panagram")
else:
  print("not panagram")
