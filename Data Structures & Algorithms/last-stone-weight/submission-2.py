from heapq import heapify_max, heappop_max, heappush_max

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)
        while len(stones) > 1:
            val = abs(heappop_max(stones) - heappop_max(stones))
            heappush_max(stones,val)
        return heappop_max(stones)