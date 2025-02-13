T=int(input("entet the number of test cases:"))
for i in range(T):
    k=int(input(f'enter the value of k:{i+1}:'))
    a=k//2
    b=k-a
    print(a*b)
