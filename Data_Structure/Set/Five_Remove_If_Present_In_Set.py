# 5. Write a Python program to remove an item from a set if it is present in the set.

my_set = {1, 2, 3, 4, 5}

item_to_remove = 4
if item_to_remove in my_set:
    my_set.remove(item_to_remove)

print(my_set)  
