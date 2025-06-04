# Last updated: 6/4/2025, 9:22:06 PM
import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()  # Sort projects by capital requirement
        
        available_projects = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(available_projects, -projects[i][1])  # store negative profit for max-heap behavior
                i += 1
            
            if available_projects:
                w -= heapq.heappop(available_projects)  # select the project with max profit
        
        return w

# Example usage:
sol = Solution()
print(sol.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))  # Output: 4
print(sol.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))  # Output: 6
