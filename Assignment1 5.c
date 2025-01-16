n=int(input("enter the number:"))
list1=[]
list2=[]
for i in range(n):
    name=input("enter the name:")
    name=name[:15]
    list1.append(name)
print(list1)
for str1 in list1:
    str2=str1[::-1]
    list2.append(str2)
print(list2)
