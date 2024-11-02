# Nested For Loop
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()
print(10 * '-')

# Nested While Loop
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1
print(10 * '-')

# Nested For-While Loop
for i in range(3):
    j = 0
    while j < 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
print(10 * '-')

# Nested While-For Loop
i = 0
while i < 3:
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()
    i += 1
print(10 * '-')

# Nested For-else Loop
for i in range(3):
    print(i)
else:
    print("Loop finished normally")

# Nested While-else Loop
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop finished normally")

# Assignment 1 - Sum of digits
data = input('Enter digits: ')
ans_sum = 0
for i in list(data):
    ans_sum += int(i)
print(f'Sum of digits {data} is: {ans_sum}')

# Assignment 2 - Table upto 12
num = int(input('Enter number: '))
for i in range(1, 13):
    print(f'{num} * {i} = {num * i}')

# Assignment 3 - ATM
user_amount = 0
while True:
    print("Select an operation:\n1. Deposit\n2. Withdraw\n3. Balance\n_. Exit\n")
    option = int(input('Enter option:'))
    if option == 1:
        amt = int(input('Enter amount:'))
        if amt % 10 != 0:
            print("Error: Amount to deposit must be in multiple of 10\n\n")
        else:
            user_amount += amt
            print(f"Success... Available Balance: {user_amount}\n\n")
    elif option == 2:
        amt = int(input('Enter amount:'))
        if user_amount < amt:
            print("Error: Insufficient amount.\n\n")
        elif (amt % 10) != 0:
            print("Error: Amount to withdraw must be in multiple of 10\n\n")
        else:
            user_amount -= amt
            print(f"Success... Available Balance: {user_amount}\n\n")
    elif option == 3:
        print(f"Balance: {user_amount}\n\n")
    else:
        print("Exited")
        break

# Assignment 4- Multiplication table
for i in range(1, 11):
    for num in range(1, 6):
        pt = f'{num} * {i} = {num * i}'
        print(f'{pt:<15}', end='\t')
    print('')

# Assignment 5- Number Pyramid
num = int(input('Enter number : '))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()
