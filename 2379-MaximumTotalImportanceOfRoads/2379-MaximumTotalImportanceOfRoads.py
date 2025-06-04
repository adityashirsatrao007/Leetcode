# Last updated: 6/4/2025, 9:18:53 PM
class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        
        degree.sort()
        importance = 0
        for i in range(n):
            importance += (i + 1) * degree[i]
        
        return importance
