l1 = []
n = 100
# Collecting 100 random numbers
for i in range(n):
    import random
    random.choice([0,1])
    l1.append(random)
count = 1

# Counting consecutive zeros
for i in range(len(l1) - 1):  # Stop before the last element
    if l1[i] == 0 and l1[i + 1] == 0:
        count += 1

print("Count of consecutive zeros:", count)
