# 12. Write a Python program to check multiple keys exists in a dictionary.

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_check = ['a', 'c', 'e']

def check_keys(dictionary, keys):
    for key in keys:
        if key not in dictionary:
            return False
    return True

if check_keys(dict, keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")