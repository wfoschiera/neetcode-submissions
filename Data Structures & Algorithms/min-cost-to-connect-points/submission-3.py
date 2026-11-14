from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        def calc_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                src, dst = tuple(points[i]), tuple(points[j])
                dist = calc_dist(src, dst)
                adj[src].append([dist, dst])
                adj[dst].append([dist, src])
        
        min_heap = []
        visit = set()
        src = tuple(points[0])
        visit.add(src)
        res = 0

        for dist, neighbor in adj[src]:
            heapq.heappush(min_heap, (dist, src, neighbor))

        # acyclic graph has (nodes-1) edges
        while len(visit) < len(points):
            dist, src, node = heapq.heappop(min_heap)

            if node in visit:
                continue
            visit.add(node)
            res += dist
            
            for dist, neighbor in adj[node]:
                if neighbor not in visit:
                    heapq.heappush(min_heap, (dist, node, neighbor))

        return res



