import random
arr = [random.randint(0, 9) for x in range(0,5)]

for x in range(0, len(arr)):
    print(f'{x} -> {arr[x]}')

