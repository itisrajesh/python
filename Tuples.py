my_tuple = (1, 2, 3, 4, 5)
print("Element at index 2:", my_tuple[2])
print("Elements from index 1 to 3:", my_tuple[1:4])
tuple2 = (6, 7, 8)
print("Concatenated tuple:", my_tuple + tuple2)
print("Repeated tuple:", my_tuple * 2)
print("Is 3 present in tuple?", 3 in my_tuple)
print("Length of tuple:", len(my_tuple))
print("Minimum value:", min(my_tuple))
print("Maximum value:", max(my_tuple))
print("Count of 2 in tuple:", my_tuple.count(2))
print("Index of 4 in tuple:", my_tuple.index(4))
my_list = list(my_tuple)
print("Tuple converted to List:", my_list)
my_set = set(my_tuple)
print("Tuple converted to Set:", my_set)
a, b, c = tuple2
print("Tuple Unpacking: a={} b={} c={}".format(a, b, c))
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested Tuple:", nested_tuple)

# Assignment 11 - Tuple Manipulation
r_tuple = input("Enter the list")
r_tuple = tuple(int(x) for x in str(r_tuple).split(","))
print("First element: ", r_tuple[0])
print("last element: ", r_tuple[-1])
print("Excluding First and Last element: ", r_tuple[1:-1])
print("Every second element: ", r_tuple[1:: 2])
print("Reverse ", r_tuple[::-1])

# Assignment 12 - Tuple packing and Unpacking
name = input("Enter: Name:")
age = int(input("Enter: Age:"))
country = input("Enter: country:")
city = input("Enter city:")
details = (name, age, (country, city))
name, age, (country, city) = details
print("Packed tuple: ", details)
print("Unpacked tuple: ", name, age, country, city)

# Assignment 13 - Tuple Statistics
r_tuple = input("Enter the list")
r_tuple = tuple(int(x) for x in str(r_tuple).split(","))
print("Sum: ", sum(r_tuple))
print("Average:", sum(r_tuple) / len(r_tuple))
print("Max:", max(r_tuple))
print("Min:", min(r_tuple))
print("Length:", len(r_tuple))

# Assignment 14: Tuple sorting Filtering
r_tuple = input("Enter the list")
r_tuple = tuple(int(x) for x in str(r_tuple).split(","))
print(tuple(sorted(list(r_tuple))))
th = int(input("Enter threshold: "))
print(tuple(filter(lambda x: x > th, r_tuple)))

# from functools import reduce

# Assignment 1: Perform Data analysis task
stud_list = []
while True:
    print(f"Enter data for student no: {len(stud_list) + 1}")
    name = input("Name: ")
    age = int(input("Age: "))
    score1 = float(input("Score1: "))
    score2 = float(input("Score2: "))
    score3 = float(input("Score3: "))
    stud_list.append((name, age, score1, score2, score3))

    option = input("Enter more details(y/n): ")
    if option == 'n':
        break

for index in range(len(stud_list)):
    avg = sum(stud_list[index][2:5]) / 3
    stud_list[index] = stud_list[index] + tuple([avg])

topper = max(stud_list, key=lambda item: item[-1])
print(f'Topper  \nName: {topper[0]} with Average: {topper[-1]}')

# print(reduce(lambda x, y: x[-1] > y[-1], stud_list))

mini = int(input("Enter minimum:"))
ans = filter(lambda x: x[-1] > mini, stud_list)
print(f"Student with marks greater than {mini}")
for st in ans:
    print(f'Name: {st[0]} with Average: {st[-1]}')

