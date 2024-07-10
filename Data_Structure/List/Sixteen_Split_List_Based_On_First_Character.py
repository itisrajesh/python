def split_list_based_on_first_character(list1):
    """
    Description: This function will split the list based on the first character of the items.
    Input: {list1 : list}
    Output: {split_list : dict}
    """
    split_list = {}
    for item in list1:
        if item[0] in split_list:
            split_list[item[0]].append(item)
        else:
            split_list[item[0]] = [item]
    return split_list


Input1 = ['apple', 'banana', 'cat', 'dog', 'elderberry', 'fig']
Input2 = ['hello', 'world', 'hello', 'python', 'world', 'code']
Input3 = ['a', 'b', 'c', 'd', 'e', 'f']
Input3 = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr']
Input4 = ['apple', 'application', 'banana', 'bear']


print(Input1, split_list_based_on_first_character(Input1), sep='\n')
print(Input2, split_list_based_on_first_character(Input2), sep='\n')
print(Input3, split_list_based_on_first_character(Input3), sep='\n')
print(Input4, split_list_based_on_first_character(Input4), sep='\n')
