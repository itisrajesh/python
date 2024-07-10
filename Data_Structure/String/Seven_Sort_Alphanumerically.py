def sort_alphanumerically():
    """
    Description: function takes input from the user and displays the unique words in sorted form (alphanumerically).
    Input: None
    Output: None
    """
    user_input = input("Enter a comma separated sequence of words: ")
    words = user_input.split(", ")
    words = list(set(words))
    words.sort()
    print(", ".join(words))


if __name__ == '__main__':
    sort_alphanumerically()