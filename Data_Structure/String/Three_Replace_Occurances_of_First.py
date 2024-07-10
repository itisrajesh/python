def change_char(str1):
    """
    Decription : Function to replace all the occurance of first character with '$' except the first character    
    Input : {str1: string}
    Output : {str1: string}
    """
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    return str1

if __name__ == '__main__':
    print(change_char('restart'))
    print(change_char('restarts'))
    print(change_char('restartss'))