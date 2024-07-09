import math

def Quadratic(a,b,c):
    """
    Description: Calculates the roots of the quadratic equation
    Input: {a:int, b:int, c:int}
    Output: {root1:int, root2:int}
    """
    delta = b*b - 4*a*c
    root1 = (-b + math.sqrt(delta))/(2*a)
    root2 = (-b - math.sqrt(delta))/(2*a)
    return root1,root2

if __name__ == '__main__':
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    result = Quadratic(a,b,c)
    print("Root 1: ",result[0])
    print("Root 2: ",result[1])