"""
Note :
    Slice notation: new_list = old_list[:]
    List constructor: new_list = list(old_list)                     
    Copy module: import copy; new_list = copy.copy(old_list)     
    Deep copy: import copy; new_list = copy.deepcopy(old_list)  # Deep copy rest are shallow copy
    List comprehension: new_list = [item for item in old_list]
    Assigning to a new variable: new_list = old_list; old_list = None
"""

def clone_list(list):
    """
    Description: Take list as ip and return the list after cloning.
    Input: {list : list}
    Output: {list : list}
    """
    return list.copy()

if __name__ == "__main__":
    list = [10, 20, 30, 20, 10, 50, 60, 40]
    print(clone_list(list))