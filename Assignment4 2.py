def check_square(num):
    x=int(num**(0.5))
    return x**2==num
def count_squaresbwrange(a,b):
    count=0
    for i in range(a,b+1):
       if check_square(i):
           count=count+1
    print("squares in the range is:",count)
T=int(input("enter the number of Test cases:"))
for i in range(T):
    a=int(input(f"enter the a{i+1} value:"))
    b=int(input(f"enter the b{i+1} value:"))
    count_squaresbwrange(a,b)
