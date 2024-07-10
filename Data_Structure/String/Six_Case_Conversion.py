
def case_conversion():
    """
    Description: function takes input from the user and displays that input back in upper and lower cases.
    Input: None
    Output: None
    """
    user_input = input("Enter a string: ")
    print("Upper case: ", user_input.upper())
    print("Lower case: ", user_input.lower())

if __name__ == '__main__':
    case_conversion()