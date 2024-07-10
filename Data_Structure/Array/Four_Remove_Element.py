def remove_occurrences(arr, element):
	"""
	Description :  Counts the number of occurrences of a specified element in an array.
    Input : { [arr], element}
    Output: None
    """
	arr.remove(element)

if __name__ == "__main__":
	arr = [1, 2, 3, 4, 1, 2, 1, 5, 1]
	for x in range(0, len(arr)):
		print(f'{x} -> {arr[x]}')
	remove_occurrences(arr, 4)
	for x in range(0, len(arr)):
		print(f'{x} -> {arr[x]}')
