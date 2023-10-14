'''
Problem 2b
'''

import math

def d(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    def min_strip(strip, min_distance, min_pair):

        strip = merge_sort(strip, 'x')
     
        for i in range(len(strip)):
            for j in range(i+1, len(strip)):
                if (strip[j][1] - strip[i][1]) >= min_distance:
                    break
                if d(strip[i], strip[j]) < min_distance:
                    min_distance = d(strip[i], strip[j])
                    min_pair = (strip[i], strip[j])
        return min_distance, min_pair
    
    def closest_pair_calc(points):
        if len(points) <= 3:
            min_distance = float('inf')
            min_points = None
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    if d(points[i], points[j]) < min_distance:
                        min_distance = d(points[i], points[j])
                        min_points = (points[i], points[j])
            return min_distance, min_points
        
        points = merge_sort(points, 'y')
    
        mid_idx = len(points) // 2
        mid_point = points[mid_idx]
        left_points = points[:mid_idx]
        right_points = points[mid_idx:]
        left_distance, left_points = closest_pair_calc(left_points)
        right_distance, right_points = closest_pair_calc(right_points)
    
        min_points = None
        
        if left_distance < right_distance:
            min_dist = left_distance
            min_points = left_points
        else:
            min_dist = right_distance
            min_points = right_points
        
        strip = []
        for i in range(len(points)):
            if abs(points[i][0] - mid_point[0]) < min_dist:
                strip.append(points[i])
    
        strip_distance, strip_pair = min_strip(strip, min_dist, min_points)
        
        if strip_distance < min_dist:
            return strip_distance, strip_pair
        else:
            return min_dist, min_points
    
    def merge_sort(points, axis):
        if len(points) <= 1:
            return points
        
        if axis == 'x':
            axis = 0
        else:
            axis = 1
        
        mid_idx = len(points) // 2
        left_lst = merge_sort(points[:mid_idx], axis)
        right_lst = merge_sort(points[mid_idx:], axis)
    
        i = 0
        j = 0
        sorted_lst = []
        
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i][axis] < right_lst[j][axis]:
                sorted_lst.append(left_lst[i])
                i += 1
            else:
                sorted_lst.append(right_lst[j])
                j += 1
        
        while i < len(left_lst):
            sorted_lst.append(left_lst[i])
            i += 1
    
        while j < len(right_lst):
            sorted_lst.append(right_lst[j])
            j += 1
        
        return sorted_lst
        
    return closest_pair_calc(points)[1]
    