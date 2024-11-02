    import math

    my_list = [1, 2, 3, 4]
    yr_list = [5,6,7]
    print(my_list + yr_list)
    copied_list = my_list.copy()
    count_of_2 = my_list.count(2)
    my_list.append(22)
    my_list.extend([5, 6])
    index_of_3 = my_list.index(3)
    my_list.insert(1, 7)
    my_list.remove(4)
    my_list.reverse()
    my_list.sort()
    print("Modified list:", my_list)

    # Assignment 8 - Generate Prime numbers
    arr_prime = []
    num = int(input("Enter a number: "))
    for i in range(2, num + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            arr_prime.append(i)
    print("Array of primes: ", arr_prime)

    # Assignment 9 - Add and remove task from list
    list_task = []
    while True:
        choice = int(input("Enter choice:\n1. Add\n2. Remove\n3. Display\n _.Exit"))
        match choice:
            case 1:
                task = input("Enter task name")
                list_task.append(task)
            case 2:
                task = input("Enter task name to remove")
                list_task.remove(task)
            case 3:
                print("Task list:", list_task)
            case _:
                break

    # Assignment 10 - Rotate array
    r_list = input("Enter the list")
    r_list = [int(x) for x in str(r_list).split(" ")]
    rotation_count = int(input("Enter rotation count : "))
    print(r_list)
    if rotation_count % len(r_list) != 0:
        for i in range(rotation_count):
            last = r_list.pop()
            r_list.insert(0, last)
    print(r_list)

