def get_smallest_element(list):
    """
    Description: Take list as input and return the smallest element from the list.
    Input: {list : list}
    Output: {smallest_element : int}
    """
    smallest_element = list[0]
    for i in list:
        if i < smallest_element:
            smallest_element = i
    return smallest_element

if __name__ == "__main__":
    list = [5, 4, 3, 0, 2, 1, 6, 7, 8, 9]
    print(get_smallest_element(list))