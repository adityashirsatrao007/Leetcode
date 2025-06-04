# Last updated: 6/4/2025, 9:21:54 PM
from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals = []
        heights = []
        max_height = 0
        result = []
        
        for left, sideLength in positions:
            right = left + sideLength
            curr_height = 0
            
            # Check intervals that overlap with the current square
            for interval_left, interval_right, interval_height in intervals:
                if left < interval_right and right > interval_left:
                    curr_height = max(curr_height, interval_height)
            
            # Update the new interval and height
            curr_height += sideLength
            intervals.append((left, right, curr_height))
            heights.append(curr_height)
            max_height = max(max_height, curr_height)
            result.append(max_height)
        
        return result
