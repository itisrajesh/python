# Write a Python function that takes two lists and returns True if they have at
# least one common member.


def is_common_element_present(list1, list2):
    """
    Description: Check if there is a common element in two lists.
    Input: {list1: list, list2: list}
    Output: {boolean: boolean}
    """
    return any(element in list2 for element in list1)

if __name__ == "__main__" :
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 6, 7, 8, 9]
    print(is_common_element_present(list1, list2))  
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    print(is_common_element_present(list1, list2))  