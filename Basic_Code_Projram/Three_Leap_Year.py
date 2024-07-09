year_input = input("Enter a year: ")
if year_input.isdigit():
    year = int(year_input)
    if year >= 1582:
        if (year % 100 == 0) and (year % 400 == 0):
            print(f"The year {year} is a leap year")
        elif (year % 4 == 0) and (year % 100 != 0):
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year} is not a leap year")
    else:
        print(f"The entered year {year} must be 1582 or later.")
else:
    print(f"Invalid year {year_input} entered. Please enter a valid year.")

