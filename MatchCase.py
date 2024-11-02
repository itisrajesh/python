fruit = "banana"

match fruit:
    case "apple":
        print("You chose a juicy red apple!")
    case "banana":
        print("You chose a long yellow banana!")
    case "cherry":
        print("You chose a small round cherry!")
    case _:
        print("You chose something else!")


print("Select an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = input("Enter your choice (1/2/3/4): ")
match choice:
    case "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} + {num2} = {num1 + num2}")
    case "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} - {num2} = {num1 - num2}")
    case "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} * {num2} = {num1 * num2}")
    case "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error! Division by zero is not allowed.")
    case _:
        print("Invalid choice.")

ch = 2
match ch:
    case 1:
        print("One")

    case 2:
        print("Two")
    case _:
        print("other")
