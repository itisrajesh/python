empty_tuple = ()
print("Empty tuple:", empty_tuple)

tuple_with_elements = (1, 2, 3, "apple", "banana")
print("Tuple with elements:", tuple_with_elements)

tuple_without_parentheses = 1, 2, 3, "apple", "banana"
print("Tuple without parentheses:", tuple_without_parentheses)

single_element_tuple = (1,)
print("Single element tuple:", single_element_tuple)

list_to_tuple = tuple([1, 2, 3, "apple", "banana"])
print("Tuple from list:", list_to_tuple)

string_to_tuple = tuple("hello")
print("Tuple from string:", string_to_tuple)

existing_tuple = (4, 5, 6)
new_tuple = tuple(existing_tuple)
print("Tuple from another tuple:", new_tuple)