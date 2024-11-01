from random import randint

# Assignment 3 - Factorial of number
# Using for loop
number = int(input("Enter number : "))
ans = 1
if number == 0:
    print(f"Factorial of number {number} is : ", ans)
else:
    for i in range(1, number + 1):
        ans *= i
    print(f"Factorial of number {number} is : ", ans)
    # Using while loop
    ans = 1
    it = 1
    while it <= number:
        ans *= it
        it += 1
    print(f"Factorial of number {number} is : ", ans)

# Assignment 4 - Calculator
print("Select an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = input("Enter your choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(num1, "+", num2, "=", num1 + num2)
elif choice == '2':
    print(num1, "-", num2, "=", num1 - num2)
elif choice == '3':
    print(num1, "*", num2, "=", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid choice.")

# Assignment 5A - Continue
number = int(input("Enter number : "))
for i in range(1, number + 1):
    if i == 5:
        continue
    else:
        print(f'{i} ', end="")

# Assignment 5B - Break
random_number = randint(1, 11)
choice = int(input("Enter choice between 1 - 10 : "))
count = 1
while True:
    choice = int(input("Enter choice between 1 - 10 : "))
    if random_number == choice or count <= 10:
        print('You won!!!')
        break
print(random_number, choice)

# Homework - Fibonacci series up to 100
a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, a + b
