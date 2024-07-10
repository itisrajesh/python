def count_strings(list):
    """
    Description: Take list as input and return the count of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
    Input: {list : list}
    Output: {count : int}
    """
    count = 0
    for i in list:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    return count

if __name__ == "__main__":
    list = ['abc', 'xyz', 'aba', '1221']
    print(count_strings(list))