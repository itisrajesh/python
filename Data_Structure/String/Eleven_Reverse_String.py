def reverse_string(str):
    """
    Description: Function to reverse a string.
    Input: {str :str}
    Output: {str :str}
    Node :
    -> [start:stop] - for slicing the string.
    -> [start:stop:step] - for slicing the string with step size.
    """
    return str[::-1]

if __name__ == '__main__':
    str = input("Enter a string: ")
    print(reverse_string(str))