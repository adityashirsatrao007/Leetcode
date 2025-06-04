# Last updated: 6/4/2025, 9:17:40 PM
from functools import lru_cache

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        answer = m * n
        
        @lru_cache(None)
        def part(up, down, left, right):
            if up == down or left == right:
                return 0
            
            min_x, max_x, min_y, max_y = down, up, right, left
            for i in range(up, down):
                for j in range(left, right):
                    if grid[i][j] == 1:
                        min_x = min(min_x, i)
                        max_x = max(max_x, i)
                        min_y = min(min_y, j)
                        max_y = max(max_y, j)
                        
            return (max_x - min_x + 1) * (max_y - min_y + 1)
        
        for x in range(m + 1):
            for y in range(n + 1):
                answer = min(answer, part(0, x, 0, n) + part(x, m, 0, y) + part(x, m, y, n))
        for x in range(m + 1):
            for y in range(n + 1):
                answer = min(answer, part(0, x, 0, y) + part(0, x, y, n) + part(x, m, 0, n))
        for x in range(m + 1):
            for y in range(n + 1):
                answer = min(answer, part(0, m, 0, y) + part(0, x, y, n) + part(x, m, y, n))
        for x in range(m + 1):
            for y in range(n + 1):
                answer = min(answer, part(0, x, 0, y) + part(x, m, 0, y) + part(0, m, y, n))
                
        for x in range(m + 1):
            for xx in range(x, m + 1):
                answer = min(answer, part(0, x, 0, n) + part(x, xx, 0, n) + part(xx, m, 0, n))
        for y in range(n + 1):
            for yy in range(y, n + 1):
                answer = min(answer, part(0, m, 0, y) + part(0, m, y, yy) + part(0, m, yy, n))
                
        return answer
        