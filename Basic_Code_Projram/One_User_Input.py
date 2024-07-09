name = input('Enter your name : ')
if len(name) > 3 and name.isalpha():
    print(f'Hello {name}')
else:
    print('Error : name either length < 3 or invalid input')
