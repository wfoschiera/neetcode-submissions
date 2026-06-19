import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Using a heap and keep it with size k
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, num)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # return heap[0]
        
        # using builtin method
        kth = heapq.nlargest(k, nums)
        return kth[-1]
