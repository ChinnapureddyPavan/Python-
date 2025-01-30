k=int(input("enter the number to check if it is a  fibonnaci or not:"))
for n in range(0,k+1):
  y=lambda n: n if n<=1 else y(n-1)+y(n-2)
  if y(n)==k:
     print("entered number is fibo")
     break
if y(n)!=k:
  print("entered number is not fibo")
