firstName = input("Enter your first name : ")
lastName = input("Enter your last name : ")

# format
print("Hi my name is {} and I'm {} year old".format(firstName, lastName))
print("Hi my name is {1} and I'm {0} year old".format(firstName, lastName))
print("Hi my name is {f_name} and I'm {l_name} year old".format(f_name = firstName, l_name = lastName))

# f-string
print(f"Hi my name is {firstName} and I'm {lastName} year old")

# seperator -> spe
print("Hello", "World", sep=" ")
print("Hello", "World", sep="-")

# endswith -> end
print("Hello", "World", end="\n\t")
print("Hello", "World", end="-\n")

# Assignment
string_one = input("Enter your first string : ")
string_two = input("Enter your last string : ")

# format
print("First String =  {} and Second String = {}".format(string_one,string_two))
print("First String =  {1} and Second String = {0} in revwerse".format(string_one,string_two))
print("First String =  {f_string} and and Second String = {s_string}".format(f_string = string_one, s_string = string_two))

# Assignment 4, 5, 6
num_one = int(input("Enter your first number : "))
num_two = int(input("Enter your last number : "))
print(f"Type of a = {type(num_one)} and b = {type(num_two)}")
print(f"Sum of a = {num_one} and b = {num_two} is {num_one+num_two}")


# Assignment 7
temp_one = int(input("Enter your first value(int) : "))
temp_two = float(input("Enter your last value(float) : "))
print(f"Type of a = {type(temp_one)} and b = {type(temp_two)}")
print(f"Sum of a = {temp_one} and b = {temp_two} is {temp_one + temp_two}")

# Assignment 8
try:
    ans = num_one + string_one
    print(f"Sum of number = {num_one} and string = {string_one} is {ans} with type {type(ans)}")
except Exception as e:
    print(e)


# Assignment 9
z = float(input("Enter float"))
print(f"Float typecased value is {z}")

# Assignment 10
PI = 3.1415
radius = int(input("Enter the radius : "))
print("Area of circle is ", PI*(radius**2))

# Assignment 11
monthly_income = float(input("Enter monthly income : "))
monthly_expenses = float(input("Enter all monthly expenses : "))
total_saving = monthly_income - monthly_expenses
percentage_saving = (total_saving/monthly_income)*100
percentage_expense = (monthly_expenses/monthly_income)*100
print(f"total saving = {total_saving}")
print(f"percentage saving={percentage_saving:.2f} percentage expense={percentage_expense:.2f}")
