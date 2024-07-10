def add_string(str1):
    """
    Decription : Function to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
    Input : {str1: string}
    Output : {str1: string}
    """
    if len(str1) < 3:
        return str1
    elif str1[-3:] == 'ing':
        return str1 + 'ly'
    else:
        return str1 + 'ing'
    
if __name__ == '__main__':
    print(add_string('abc'))
    print(add_string('string'))
