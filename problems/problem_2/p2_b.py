'''
Problem 2b
'''

import math

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
     
    def p2_a(points):
        n_points = len(points)
        min_points = [(0,0),(0,0)]
        min_distance = float('inf')
        for i in range(n_points):
            for j in range(i+1, n_points):
                if d(points[i],points[j]) < min_distance:
                    min_points = [points[i],points[j]]
                    min_distance = d(points[i],points[j])
    
        return min_points, min_distance
     
     
    def divide_and_conqure(points_sorted, n):
        if n <= 3:
            return p2_a(points_sorted)

        mid_point = points_sorted[n//2] 
        
        left_points, left_distance = divide_and_conqure(points_sorted, n//2)
        right_points, right_distance = divide_and_conqure(points_sorted[n//2:], n - n//2)

        if right_distance > left_distance:
            min_points = left_points
            min_distance = left_distance
        else:
            min_points = right_points
            min_distance = right_distance
        
        strip = []
        
        for i in range(n):
            if abs(points_sorted[i][0] - mid_point[0]) < min_distance:
                strip.append(points_sorted[i])

        strip = sorted(strip, key=lambda x: x[1])
        
        for i in range(len(strip)):
            for j in range(i+1, len(strip)):
                if (strip[j][1] - strip[i][1]) >= min_distance:
                    break
                    
                if d(strip[i], strip[j]) < min_distance:
                    min_distance = d(strip[i], strip[j])
                    min_points = [strip[i], strip[j]]

        return (min_points, min_distance)
     
    points_sorted = sorted(points, key=lambda x: x[0])

    min_points, min_distance = divide_and_conqure(points_sorted, len(points))

    return min_points
    