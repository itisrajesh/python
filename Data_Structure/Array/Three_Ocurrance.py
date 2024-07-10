def count_occurrences(arr, element):
    """
    Description :  Counts the number of occurrences of a specified element in an array.
    Input : { [arr], element}
    Output: {count}
    """
    count = 0
    for item in arr:
        if item == element:
            count += 1
    return count


if __name__ == "__main__":
    array = [1, 2, 3, 4, 1, 2, 1, 5, 1]
    element_to_count = 1
    print(f"The number of occurrences of {element_to_count} in the array is: {count_occurrences(array, element_to_count)}")
 
