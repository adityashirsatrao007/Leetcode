# Last updated: 6/4/2025, 9:21:50 PM
class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        memo = [[[-1] * n for _ in range(n)] for _ in range(n)]
        
        def dfs(x1, y1, x2):
            y2 = x1 + y1 - x2
            if x1 >= n or y1 >= n or x2 >= n or y2 >= n:
                return -float('inf')
            if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                return -float('inf')
            if x1 == n-1 and y1 == n-1:
                return grid[x1][y1]
            if memo[x1][y1][x2] != -1:
                return memo[x1][y1][x2]
            
            cherries = grid[x1][y1]
            if x1 != x2 or y1 != y2:
                cherries += grid[x2][y2]
            
            max_cherries = max(dfs(x1+1, y1, x2), dfs(x1, y1+1, x2), dfs(x1+1, y1, x2+1), dfs(x1, y1+1, x2+1))
            
            memo[x1][y1][x2] = cherries + max_cherries
            
            return memo[x1][y1][x2]
        
        return max(0, dfs(0, 0, 0))
