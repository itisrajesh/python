# 13. Write a Python program to count number of items in a dictionary value that is a list.

dict = {'a': [1, 2, 3], 'b': [4, 5, 6, 7], 'c': [8, 9]}

def count_items(dictionary):
    count = 0
    for value in dictionary.values():
        if isinstance(value, list):
            count += len(value)
    return count

item_count = count_items(dict)

print(f"Number of items in the dictionary values: {item_count}")
