# Last updated: 6/4/2025, 9:19:10 PM
from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.result = 0
        self.graph = defaultdict(list)

    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        for u, v, t in edges:
            self.graph[u].append((v, t))
            self.graph[v].append((u, t))

        visited = [0] * len(values)
        self.backtrack(values, visited, 0, 0, 0, maxTime)
        return self.result

    def backtrack(self, values: List[int], visited: List[int], idx: int, time: int, value: int, maxTime: int) -> None:
        if time > maxTime:
            return
        if visited[idx] == 0:
            value += values[idx]
        if idx == 0:
            self.result = max(self.result, value)
        visited[idx] += 1
        for neighbor, t in self.graph[idx]:
            self.backtrack(values, visited, neighbor, time + t, value, maxTime)
        visited[idx] -= 1