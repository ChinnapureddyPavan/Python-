L=int(input('enter the number 1:'))
R=int(input('enter the number 2:'))
d=float("-inf")
max1=0
for i in range(L,R+1):
    for j in range(L,R+1):
        max1=i^j
        if(max1>d):
            d=max1
print(d)
          
       

        
