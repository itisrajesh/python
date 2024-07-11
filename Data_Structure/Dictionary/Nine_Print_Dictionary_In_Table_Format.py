# 9. Write a Python program to print a dictionary in table format.

def print_dictionary_table(dictionary):
    print("{:<15} {:<15}".format("Key", "Value"))
    print("------------------------")
    for key, value in dictionary.items():
        print("{:<15} {:<15}".format(key, value))

my_dictionary = {"Name": "John", "Age": 30, "City": "New York"}
print_dictionary_table(my_dictionary)