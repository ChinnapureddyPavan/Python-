word=list(input("enter the word:"))
for i in range(len(word)):
    if i%2!=0:
        word[i]= word[i].capitalize()
    else:
        word[i]=word[i]
        
print(''.join(word))
