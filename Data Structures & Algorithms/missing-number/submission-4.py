class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
    
        for i, n in enumerate(nums):
            if i == len(nums) - 1:
                return n + 1
            if n + 1 != nums[n+1]:
                return n+1

        
