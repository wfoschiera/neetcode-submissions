class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            idx = abs(num) -1 
            if nums[idx] < 0:
                return num
            nums[idx] *= -1