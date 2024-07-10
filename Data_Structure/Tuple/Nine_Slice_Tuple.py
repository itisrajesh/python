# Write a Python program to slice a tuple.

# Slice a tuple in various ways

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slice a tuple from the beginning
sliced_tuple = my_tuple[:5]
print(sliced_tuple)  

# Slice from a specific index to the end
sliced_tuple = my_tuple[5:]
print(sliced_tuple)  

# Slice a specific range
sliced_tuple = my_tuple[3:7]
print(sliced_tuple)  

# Slice with a step
sliced_tuple = my_tuple[::2]
print(sliced_tuple)  

# Slice with a negative index
sliced_tuple = my_tuple[-5:]
print(sliced_tuple)  