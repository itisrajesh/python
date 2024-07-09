import random

times = input('Enter number of Times you want to flip : ')

if not times.isnumeric  and not times.isdigit():
    print('Invalid user input')
    exit()

for i in range(0,int(times)):
    print(f'{ random.random() < 0.5 and "Tails" or "Head"}')



