sets=[]
for i in range(1,6):
    seti={i}
    j=i
    while j<=10000:
       j=j+5
       if j<=10000:
         seti.add(j)
    sets.append(seti)
print(sets)
