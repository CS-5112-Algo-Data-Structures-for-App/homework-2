'''
Problem 2c
'''

import math
from collections import defaultdict

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    if len(points) <= 3:
        min_distance = float('inf')
        min_points = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if d(points[i], points[j]) < min_distance:
                    min_distance = d(points[i], points[j])
                    min_points = (points[i], points[j])
        return min_points
        
    def make_grid_dictionary(points, dPrime):
        grid = defaultdict(list)
        
        for point in points:
            x = int(point[0] // dPrime)
            y = int(point[1] // dPrime)
            grid[(x, y)].append(point)
            
        return grid
        
    min_distance = d(points[0], points[1])
    min_points = (points[0], points[1])
    grid = make_grid_dictionary(points[:2], min_distance / 2)
    
    for i in range(2, len(points)):
        x, y = points[i]
        x_half_distance = int(x // (min_distance / 2))
        y_half_distance = int(y // (min_distance / 2))
        points_in_range = []
        
        for x_grid in range(-2, 3):
            for y_grid in range(-2, 3):
                if (x_half_distance + x_grid, y_half_distance + y_grid) in grid:
                    points_in_range.extend(grid[(x_half_distance + x_grid, y_half_distance + y_grid)])

        new_min_distance = min_distance
        for point in points_in_range:
            
            if d(points[i], point) < new_min_distance:
                new_min_distance = dist = d(points[i], point)
                min_points = (points[i], point)
                break
    
        if new_min_distance < min_distance:
            min_distance = new_min_distance
            grid = make_grid_dictionary(points[:i+1], min_distance / 2)
        else:
            grid[(x_half_distance, y_half_distance)].append(points[i])
            
    return min_points