class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        kth = heapq.nlargest(k, nums)
        return kth[-1]