list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

difference = list(set1 - set2)

print("Difference:", difference)



list1 = [11, 12, 13, 14, 15]
list2 = [13, 14, 15, 16, 17]
difference = []
# Difference using list comprehension
for x in list1:
    if x not in list2:
        difference.append(x)

print("Difference:", difference)