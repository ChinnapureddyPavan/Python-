n=int(input("enter the no of test cases:"))
list1=[]
for i in range(n):
    num=int(input(""))
    list1.append(num)
print("output:")

for numbers in list1:
    count=0
    m=numbers
    while m>0:
        rem=m%10
        if numbers%rem==0:
            count+=1
        m=m//10
    print(count)
        
