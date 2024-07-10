def remove_duplicates(list):
    """
    Description: Take list as ip and return the list after removing duplicates.
    Input: {list : list}
    Output: {list : list}
    """
    return list(set(list))

if __name__ == "__main__":
    list = [10, 20, 30, 20, 10, 50, 60, 40]
    print(remove_duplicates(list))
    