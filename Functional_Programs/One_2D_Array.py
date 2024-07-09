import array

def print_arr(arr, rows, cols):
    for i in range(0, rows):
        for j in range(0, cols):
            print(arr[i][j], end= " ")
        print('\n')


def input_array(arr, rows, cols):
    for i in range(0, rows):
        for j in range(0, cols):
            arr[i][j] = int(input(f"Enter value for row : {i} col : {j} :"))

if __name__ == "__main__":
    rows = int(input('Enter number of rows :'))
    cols = int(input('Enter number of columns :'))
    two_d_array = [array.array('i', [0] * cols) for _ in range(rows)]
    input_array(two_d_array, rows, cols)
    print_arr(two_d_array, rows, cols)


