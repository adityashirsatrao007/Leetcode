# Last updated: 6/4/2025, 9:18:42 PM
from collections import defaultdict, deque

class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def topological_sort(graph, k):
            in_degree = {i: 0 for i in range(1, k + 1)}
            for node in graph:
                for neighbor in graph[node]:
                    in_degree[neighbor] += 1
            
            queue = deque([node for node in range(1, k + 1) if in_degree[node] == 0])
            order = []
            
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(order) == k:
                return order
            else:
                return []

        row_graph = defaultdict(list)
        col_graph = defaultdict(list)
        
        for above, below in rowConditions:
            row_graph[above].append(below)
        
        for left, right in colConditions:
            col_graph[left].append(right)
        
        row_order = topological_sort(row_graph, k)
        col_order = topological_sort(col_graph, k)
        
        if not row_order or not col_order:
            return []
        
        position = {num: (i, j) for i, num in enumerate(row_order) for j, col_num in enumerate(col_order) if col_num == num}
        
        matrix = [[0] * k for _ in range(k)]
        
        for num, (r, c) in position.items():
            matrix[r][c] = num
        
        return matrix
