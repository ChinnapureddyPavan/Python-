T=int(input("enter the number of test cases:"))
for i in range(1,T+1):
    N=int(input(f"enter the no of cycles for {i}:"))
    heigth_of_tree=1
    for j in range(1,N+1):
       if j%2!=0:
          heigth_of_tree*=2
       else:
         heigth_of_tree+=1
    print(heigth_of_tree)
