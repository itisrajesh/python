# 11. Write a Python program to use of frozensets.

frozen_set = frozenset([1, 2, 3, 4, 5])

print(frozen_set)  

frozen_set.add(6)  # AttributeError

new_frozen_set = frozen_set.union([6, 7, 8])
print(new_frozen_set)

dictionary = {frozen_set: "Hello"}
print(dictionary)  
