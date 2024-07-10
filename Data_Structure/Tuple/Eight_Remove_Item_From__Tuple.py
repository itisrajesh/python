def remove_item(my_tuple, item):
    return tuple(x for x in my_tuple if x != item)

my_tuple = (1, 2, 3, 4, 5)
new_tuple = remove_item(my_tuple, 3)
print(new_tuple)  