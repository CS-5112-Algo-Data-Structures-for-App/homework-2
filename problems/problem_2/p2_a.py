'''
Problem 2a
'''

import math

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    n_points = len(points)
    min_points = [(0,0),(0,0)]
    min_distance = float('inf')
    for i in range(n_points):
        for j in range(i+1, n_points):
            if d(points[i],points[j]) < min_distance:
                min_points = [points[i],points[j]]
                min_distance = d(points[i],points[j])

    return min_points

if __name__ == '__main__':
    input_2 = [
    [0.47, 0.53],
    [0.99, 0.54],
    [0.4,  0.57],
    [0.83, 0.19],
    [0.73, 0.1 ],]

    print(closest_pair(input_2))
