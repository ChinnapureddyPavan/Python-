n=int(input("enter the number:"))
print("reverse of the number:")
while n>0:
    rem=n%10
    print(rem,end="")
    n=n//10
