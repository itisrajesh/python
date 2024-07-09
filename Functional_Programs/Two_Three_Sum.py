import array

def input_array(arr, size):
    for i in range(0, size):
        arr[i] = int(input(f"Enter value for element at{i+1} : "))

def print_array(arr, size):
    for i in range(0, size):
        print(f"Value at {i+1}th element : {arr[i]}")

def three_sum(arr, size):
    found = set()
    for i in range(0, size):
        for j in range(i+1, size):
            for k in range(j+i, size):
                if  arr[i] + arr[j] + arr[k] == 0:
                    found.add(tuple(sorted((arr[i], arr[j], arr[k]))))
    return found

if __name__ == "__main__":
    size = int(input('Enter size of array : '))
    arr = array.array('i', [0] * size) 
    input_array(arr, size)
    print_array(arr, size)
    
    found = three_sum(arr, size)
    if len(found) == 0:
        print("No triplets found")
    else:
        print(f"Total Triplets with sum zero are : {found.__len__()}")
        print(f"Triplets with sum zero are : {found}")

