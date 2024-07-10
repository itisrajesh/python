def multiplication_of_element(list):
    """
    Description: Take list as input and return the multiplication of all the elements in the list.
    Input: {list : list}
    Output: {sum : int}
    """
    ans = 1
    for i in list:
        ans *= i
    return ans

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    print(multiplication_of_element(list)) 