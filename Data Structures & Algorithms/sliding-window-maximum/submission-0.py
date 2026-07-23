class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i + k <= len(nums):
                sliced = nums[i:i+k]
                res.append(max(sliced)) 
        return res