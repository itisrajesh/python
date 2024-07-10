def last_part_of_string():
    """
    Description: function takes input from the user and displays the last part of a string before a specified character.
    Input: None
    Output: None
    """
    user_input = input("Enter a string: ")
    specified_character = input("Enter a specified character: ")
    specified_character_index = user_input.index(specified_character)
    print(user_input[:specified_character_index])
    
    # print(user_input.split(specified_character)[0])
    
if __name__ == '__main__':
    last_part_of_string()