list1=[]
n=int(input("enter the number:"))
for i in range(n):
  if i**2 < n:
      list1.append(i**2)
print(list1)
