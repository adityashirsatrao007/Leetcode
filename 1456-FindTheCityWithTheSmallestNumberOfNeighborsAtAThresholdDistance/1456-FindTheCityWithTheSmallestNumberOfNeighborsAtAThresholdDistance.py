# Last updated: 6/4/2025, 9:20:33 PM
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        from collections import defaultdict
    # STEP 1
        adj = defaultdict(list)
        for v1, v2, dist  in edges:
            adj[v1].append((v2,dist))  
            adj[v2].append((v1,dist))  
    # STEP 2    
        def dijkstra(src):
            heap = [(0,src)]
            visit = set()
    # STEP 3
            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit: continue
                visit.add(node)
    # STEP 4
                for nei,dist2 in adj[node]:
                    nei_dist = dist + dist2
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap,(nei_dist,nei)) 
    # STEP 5
            return len(visit)-1
    # STEP 6
        res, min_count = -1, n 
        for node in range(n):
    # STEP 7
            count = dijkstra(node)
            if count <= min_count:
                res = node
                min_count = count
        return res