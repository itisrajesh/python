# 15. Write a Python program to find common items from two lists.
def common_items_method_1(list1, list2):
    """
    Description: This function will return the common items from two lists.
    Input: {list1 : list, list2 : list}
    Output: {common_items : list}
    """
    return list(set(list1) & set(list2))

def common_items_method_2(list1, list2):
    """
    Description: This function will return the common items from two lists.
    Input: {list1 : list, list2 : list}
    Output: {common_items : list}
    """
    common_items = []
    for item in list1:
        if item in list2:
            common_items.append(item)
    return common_items

def common_items_method_3(list1, list2):
    """
    Description: This function will return the common items from two lists.
    Input: {list1 : list, list2 : list}
    Output: {common_items : list}
    """
    return [item for item in list1 if item in list2]

print(common_items_method_1([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_items_method_2([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_items_method_3([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))