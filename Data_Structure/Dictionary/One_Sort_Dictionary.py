# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

dict = {'a': 4, 'b': 2, 'c': 1, 'd': 3}

# ascending order
sorted_dict = dict.items()
sorted_dict = sorted(sorted_dict, key = lambda x: x[1])
print(sorted_dict)

# descending order
sorted_dict = dict.items()
sorted_dict = sorted(sorted_dict, key = lambda x: x[1], reverse = True)
print(sorted_dict)