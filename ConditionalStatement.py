score = 91
attendance = 80
if score >= 90:
    if attendance >= 90:
        print("Grade: A, Honors")
    else:
        print("Grade: A")
elif score >= 80:
    if attendance >= 90:
        print("Grade: B, Honors")
    else:
        print("Grade: B")
else:
    print("Grade: C")

# Assignment 1 - Check year is leap year on not
year = int(input("Enter year : "))
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")

# Assignment 2 - Strength of password
password = str(input("Enter the password : "))
c1 = len(password) > 8
c2 = any(char.isupper() for char in password) and any(char.islower() for char in password)
c3 = any(char.isdigit() for char in password)
special = ['!', '@', '#', '$']
c4 = any(char in special for char in password)
strength = [c1, c2, c3, c4]
strength_ans = strength.count(True)
if strength_ans == 1:
    print("Weak")
elif strength_ans == 2 or strength_ans == 3:
    print("Moderate")
elif strength_ans == 4:
    print("Strong")


# Assignment 3: Ticket price based on age
age = int(input("Enter age"))
price = 0
if age <= 5:
    price = "free"
elif 5 < age <= 12:
    price = 5
elif 12 < age <= 60:
    price = 10
elif age > 60:
    price = 7
print("Price = ", price)
