
def count_occurrences_of_substring():
    """
    Description: function to count occurrences of a substring in a string.
    Input: None
    Output: None
    """
    user_input = input("Enter a string: ")
    substring = input("Enter a substring: ")
    print(user_input.count(substring))

if __name__ == '__main__':
    count_occurrences_of_substring()