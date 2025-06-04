# Last updated: 6/4/2025, 9:21:28 PM
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        size = n * 3
        graph = [[0] * size for _ in range(size)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    graph[i * 3][j * 3 + 2] = 1
                    graph[i * 3 + 1][j * 3 + 1] = 1
                    graph[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    graph[i * 3][j * 3] = 1
                    graph[i * 3 + 1][j * 3 + 1] = 1
                    graph[i * 3 + 2][j * 3 + 2] = 1

        def dfs(x, y):
            if 0 <= x < size and 0 <= y < size and graph[x][y] == 0:
                graph[x][y] = 1
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

        regions = 0
        for i in range(size):
            for j in range(size):
                if graph[i][j] == 0:
                    dfs(i, j)
                    regions += 1

        return regions
