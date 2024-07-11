# 6. Write a Python program to remove a key from a dictionary.

# Method 1
dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
key = 3
if key in dict:
    del dict[key]

print(dict)




# Method 2
dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
key = 3
dict.pop(key)
print(dict)


# Method 3
dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
key = 3
dict.setdefault(key, None)
del dict[key]
print(dict)






