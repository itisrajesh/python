# Write a python program to check whether two lists are circularly identical.

def check_circular_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    
    list1 = list1 * 2
    for i in range(len(list1)):
        if list1[i] == list2[0]:
            for j in range(len(list2)):
                if list1[i + j] != list2[j]:
                    break
            else:
                return True
    return False

print(check_circular_identical([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))