# Write a Python program to find the repeated items of a tuple.
def find_repeated_items(my_tuple):
    repeated_items = []
    for item in my_tuple:
        if my_tuple.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items

my_tuple = (1, 2, 3, 2, 4, 5, 5, 6)
print(find_repeated_items(my_tuple))  