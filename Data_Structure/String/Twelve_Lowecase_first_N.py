def lowercase_first_n_characters(str, n):
    """
    Description: Function to lowercase first n characters in a string.
    Input: {str :str, n :int}
    Output: {str :str}
    """
    return str[:n].lower() + str[n:]

if __name__ == '__main__':
    str = input("Enter a string: ")
    n = int(input("Enter the n : "))
    print(lowercase_first_n_characters(str, n))