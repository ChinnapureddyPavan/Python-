sets=[]
for i in range(1,6):
    seti={i}
    j=i
    while j<=10 :
       j=j+5
       if j<=10:
        seti.add(j)
    sets.append(seti)
print(sets)
