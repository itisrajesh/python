def longest_string(lst):
    """
    Decription : Function to return the length of the longest string from a list of strings.
    Input : {lst: list}
    Output : {int}
    """
    lenths = [len(i) for i in lst]
    return max(lenths)

if __name__ == '__main__':
    print(longest_string(['abc', 'string', 'python', 'csdksdnsd', 'dsi']))