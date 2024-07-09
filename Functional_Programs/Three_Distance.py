import sys
import math

def euclidean_distance(x, y):
    """
    Description: Calculates the Euclidean distance between two points.
    Input: {x:int, y:int} 
    Output: {Euclidean distance : fload} 
    """
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


x = int(sys.argv[1])
y = int(sys.argv[2])

print(round(euclidean_distance(x, y), 2))
