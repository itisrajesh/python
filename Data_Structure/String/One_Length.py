def string_length(str1):
    """"
    Description : This function is used to find the length of the string
    Input : {str1 : string}
    Output : {count : int}
    """
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('Rajesh'))