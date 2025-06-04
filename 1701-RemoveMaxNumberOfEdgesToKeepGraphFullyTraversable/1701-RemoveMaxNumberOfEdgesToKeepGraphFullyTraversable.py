# Last updated: 6/4/2025, 9:20:00 PM
class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent_a = list(range(n+1))
        parent_b = list(range(n+1))
        
        def find(parent, u):
            if parent[u] != u:
                parent[u] = find(parent, parent[u])
            return parent[u]
        
        def union(parent, u, v):
            pu = find(parent, u)
            pv = find(parent, v)
            if pu != pv:
                parent[pu] = pv
                return True
            return False
        
        edges.sort(reverse=True, key=lambda x: x[0])
        
        res = 0
        e1 = e2 = 0
        for t, u, v in edges:
            if t == 3:
                if union(parent_a, u, v):
                    union(parent_b, u, v)
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
            elif t == 1:
                if union(parent_a, u, v):
                    e1 += 1
                else:
                    res += 1
            elif t == 2:
                if union(parent_b, u, v):
                    e2 += 1
                else:
                    res += 1
        
        if e1 == n-1 and e2 == n-1:
            return res
        return -1
