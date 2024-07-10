import random
arr = [random.randint(0, 9) for x in range(0,5)]
for x in range(0, len(arr)):
    print(f'{x} -> {arr[x]}')

arr.reverse()

for x in range(0, len(arr)):
    print(f'{x} -> {arr[x]}')

for i in range(0, (len(arr)//2)):
    arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]  

for x in range(0, len(arr)):
    print(f'{x} -> {arr[x]}')


