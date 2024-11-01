#Method 1
a, b  = 11, 12
print("a = ", a, "b = ", b )
c = a
a = b
b = c
print("a = ", a, "b = ", b )


#Method 2
a, b  = 11, 12
print("a = ", a, "b = ", b )
a, b = b, a
print("a = ", a, "b = ", b )
