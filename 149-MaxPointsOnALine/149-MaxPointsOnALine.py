# Last updated: 6/4/2025, 9:23:01 PM
from fractions import Fraction
from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        
        max_points = 0
        
        for i in range(len(points)):
            slope_count = defaultdict(int)
            duplicate = 1  # count the duplicate points
            
            for j in range(len(points)):
                if i != j:
                    if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                        duplicate += 1
                    else:
                        slope = self.calculate_slope(points[i], points[j])
                        slope_count[slope] += 1
            
            current_max = duplicate  # max points on the same line through points[i]
            for count in slope_count.values():
                current_max = max(current_max, count + duplicate)
            
            max_points = max(max_points, current_max)
        
        return max_points
    
    def calculate_slope(self, p1, p2):
        if p1[0] == p2[0]:
            return float('inf')
        else:
            return Fraction(p2[1] - p1[1], p2[0] - p1[0])
