# Write a Python program to sum all the items in a list.

def sum_of_element(list):
    """
    Description: Take list as input and return the sum of all the elements in the list.
    Input: {list : list}
    Output: {sum : int}
    """
    sum = 0
    for i in list:
        sum += i
    return sum

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    print(sum_of_element(list)) 