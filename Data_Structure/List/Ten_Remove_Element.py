def remove_elements(list):
    """
    Description: Remove 0th, 4th and 5th elements from the list.
    Input: {list: list}
    Output: {list: list}
    """
    list.pop(5)
    list.pop(4)
    list.pop(0) 
    return list

if __name__ == "__main__":
    list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print(remove_elements(list))