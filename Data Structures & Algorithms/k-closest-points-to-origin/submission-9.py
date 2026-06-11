import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ### one line solution O(nlogn) ###
        # return sorted(points, key=lambda x: (x[0]**2 + x[1]**2)**(1/2))[:k]

        ### using heapq ###
        # hq = []
        # for point in points:
        #     x, y = point
        #     distance = (x**2 + y**2)  # avoid additional computation.
        #     entry = [distance, point]
        #     heapq.heappush(hq, entry)
        # smallest =  heapq.nsmallest(k, hq)
        # return [point for distance, point in smallest]

        ### using max heap ###
        # the distance will be the inverse. Higher distances stays on top of heap

        hq = []
        for point in points:
            distance = -(point[0]**2 + point[1]**2)
            entry = [distance, point]
            heapq.heappush(hq, entry)
            if len(hq) > k:
                # keep len(heap) == k
                heapq.heappop(hq)

        return [point for distance, point in hq]