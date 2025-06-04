# Last updated: 6/4/2025, 9:22:52 PM
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        
        dp = [[float('inf')] * n for _ in range(m)]
        
        # Starting point: princess room
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        
        # Fill the dp table from bottom-right to top-left
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if i + 1 < m:
                    dp[i][j] = min(dp[i][j], max(1, dp[i+1][j] - dungeon[i][j]))
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], max(1, dp[i][j+1] - dungeon[i][j]))
        
        return dp[0][0]
