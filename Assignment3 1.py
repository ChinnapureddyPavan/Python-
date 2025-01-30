def digital_root(n):
    m=n
    while m>9:
        sum=0
        k=m
        while k>0:
            sum+=k%10
            k=k//10
        m=sum
    print("digital root of the entered number is:",sum)
n=int(input("enter the number:"))  
digital_root(n)
