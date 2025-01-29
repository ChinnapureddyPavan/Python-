def spliting_from_right(s,seperator,n):
    list1=[]
    current=""
    for i in range(len(s)-1,-1,-1):
          if s[i]==seperator and n>0:
              if current:
                  list1.append(current)
                  current=""
                  n=n-1
          else:
              current = s[i]+current
    if current:
        list1.append(current)
    return list1[::-1]
    
s="pavan kumar reddy"
seperator=" "
n=int(input("enter the number of splits to do:"))
result=spliting_from_right(s,seperator,n)
print(result)
