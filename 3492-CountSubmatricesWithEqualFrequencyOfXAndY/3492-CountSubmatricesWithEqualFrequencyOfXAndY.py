# Last updated: 6/4/2025, 9:17:27 PM
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        cnt1 = [[1 if grid[i][j] == 'X' else 0 for j in range(m)] for i in range(n)]
        cnt2 = [[1 if grid[i][j] == 'Y' else 0 for j in range(m)] for i in range(n)]
        
        for i in range(1, n):
            for j in range(m):
                cnt1[i][j] += cnt1[i-1][j]
                cnt2[i][j] += cnt2[i-1][j]
        
        for i in range(n):
            for j in range(1, m):
                cnt1[i][j] += cnt1[i][j-1]
                cnt2[i][j] += cnt2[i][j-1]
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if cnt1[i][j] and cnt1[i][j] == cnt2[i][j]:
                    ans += 1
        return ans