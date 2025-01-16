a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
print("before swapping:")
print(f"a:{a} b:{b}")
print("after swaping:")
a=a+b
b=a-b
a=a-b
print(f"a:{a} b:{b}")
