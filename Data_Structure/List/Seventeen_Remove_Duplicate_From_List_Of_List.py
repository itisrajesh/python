def remove_duplicate_from_list_of_list(list):
    """
    Description: This function will remove duplicates from a list of lists.
    Input: {list : list[list]}
    Output: {output : list[list]}
    """
    output = []
    for item in list:
        print(item, output, sep=' : ')
        if item not in output:
            output.append(item)
    return sorted(output)

Input = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(Input, remove_duplicate_from_list_of_list(Input), sep='\n')
