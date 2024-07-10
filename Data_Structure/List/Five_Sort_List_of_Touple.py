def sort_list_of_touple(list):
    """
    Description: Take list as input and return the list sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
    Input: {list : list}
    Output: {sorted_list : list}
    """
    return sorted(list, key = lambda x: x[ -1])

if __name__ == "__main__":
    list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_list_of_touple(list))