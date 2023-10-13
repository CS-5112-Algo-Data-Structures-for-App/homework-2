'''
Problem 2c
'''

import math
from collections import defaultdict

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def closest_pair(points):
    min_distance = d(points[0], points[1])
    min_points = [points[0], points[1]]

    
    




if __name__ == '__main__':
    input_2 = [
    [0.47, 0.53],
    [0.99, 0.54],
    [0.4,  0.57],
    [0.83, 0.19],
    [0.73, 0.1 ],
]

    print(closest_pair(input_2))