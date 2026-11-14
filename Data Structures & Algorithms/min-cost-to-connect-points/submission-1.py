import heapq
from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        adj = defaultdict(list)
        for src in points:
            for dest in points:
                if src == dest:
                    continue
                src, dest = tuple(src), tuple(dest)
                dist = distance(src, dest)
                adj[src].append((dest, dist))
        
        src = tuple(points[0])
        # mst = []
        visit = set()      
        visit.add(src)
        min_heap = []
        res = 0
        for neighbor, dist in adj[src]:
            heapq.heappush(min_heap, (dist, src, neighbor))
        
        while len(visit) < len(points):
            dist, src, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            
            visit.add(node)
            res += dist
            for neighbor, dist in adj[node]:
                if neighbor not in visit:
                    heapq.heappush(min_heap, (dist, node, neighbor))
        return res
