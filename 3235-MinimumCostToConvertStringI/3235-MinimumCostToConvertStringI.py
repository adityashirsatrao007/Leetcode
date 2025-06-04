# Last updated: 6/4/2025, 9:17:59 PM
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        import sys
        from collections import defaultdict
        
        if len(source) != len(target):
            return -1
        
        # Initialize the graph with a high value indicating no direct transformation
        inf = float('inf')
        graph = defaultdict(lambda: defaultdict(lambda: inf))
        
        # Fill the graph with given transformations
        for o, c, z in zip(original, changed, cost):
            graph[o][c] = min(graph[o][c], z)  # take the minimum cost if multiple exist

        # Use Floyd-Warshall algorithm to find the minimum cost to transform any char to any other char
        chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        for k in chars:
            for i in chars:
                for j in chars:
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]

        # Calculate the minimum cost to convert source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            min_cost = graph[s_char][t_char]
            if min_cost == inf:
                return -1
            total_cost += min_cost
        
        return total_cost

# Example usage:
source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2, 5, 5, 1, 2, 20]

solution = Solution()
print(solution.minimumCost(source, target, original, changed, cost))  # Output: 28
