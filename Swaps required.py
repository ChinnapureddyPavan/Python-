num = int(input("Enter the number of elements: "))
l = list(map(int, input("Enter the elements separated by space: ").split()))
sorted_list = sorted(l)
print("Sorted List:", sorted_list)

l1 = l[:] # Copying the original list to l1
print("Original List Copy:", l1)

swaps = 0
for i in range(len(l)):
    while l1[i] != sorted_list[i]:
        correct_index = l1.index(sorted_list[i])
        # Swapping the elements to match the sorted list
        l1[i], l1[correct_index] = l1[correct_index], l1[i]
        swaps += 1

print("Total Swaps Required:", swaps)
