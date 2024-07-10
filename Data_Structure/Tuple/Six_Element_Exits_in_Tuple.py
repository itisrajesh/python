
def check_element_exists_in_tuple_1(element, tuple):
    return element in tuple

def check_element_exists_in_tuple_2(element, tuple):
    return tuple.count(element) > 0

print(check_element_exists_in_tuple_1(5, (1, 2, 3, 4, 5)))
print(check_element_exists_in_tuple_2(6, (1, 2, 3, 4, 5)))