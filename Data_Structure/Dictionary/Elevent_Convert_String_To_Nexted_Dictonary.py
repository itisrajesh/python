# 11. Write a Python program to convert a list into a nested dictionary of keys.

def convert_list_to_nested_dict(lst):
    result = {}
    current_dict = result

    for key in lst[:-1]:
        current_dict[key] = {}
        current_dict = current_dict[key]

    current_dict[lst[-1]] = None

    return result

lst = ['a', 'b', 'c', 'd']
nested_dict = convert_list_to_nested_dict(lst)
print(nested_dict)