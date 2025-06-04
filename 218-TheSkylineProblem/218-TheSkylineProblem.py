# Last updated: 6/4/2025, 9:22:41 PM
from heapq import *

class Solution:
    def getSkyline(self, buildings):
        events = [(l, -h, r) for l, r, h in buildings]
        events += [(r, 0, 0) for _, r, _ in buildings]
        events.sort()
        
        result = [[0, 0]]
        active_heights = [(0, float('inf'))]
        
        for l, neg_h, r in events:
            while l >= active_heights[0][1]:
                heappop(active_heights)
            if neg_h:
                heappush(active_heights, (neg_h, r))
            if result[-1][1] != -active_heights[0][0]:
                result.append([l, -active_heights[0][0]])
        
        return result[1:]
