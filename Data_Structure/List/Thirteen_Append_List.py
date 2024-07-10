# 13. Write a Python program to append a list to the second list.

def append_list_method_1(list1, list2):
    list1.extend(list2)
    return list1

def append_list_method_2(list1, list2):
    return list1 + list2

def append_list_method_3(list1, list2):
    for elem in list2:
        list1.append(elem)
    return list1

print(append_list_method_1([1, 2, 3], [4, 5, 6]))
print(append_list_method_2([1, 2, 3], [4, 5, 6]))
print(append_list_method_3([1, 2, 3], [4, 5, 6]))
