def count_character(str1):
    """
    Description : This function is used to count the number of characters in a string
    Input : {str1 : string}
    Output : {count : dict}
    """
    count = {}
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

if __name__ == '__main__':
    print(count_character('google.com'))
