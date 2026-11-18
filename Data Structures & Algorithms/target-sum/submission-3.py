from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def helper(i, rest):
            if i == len(nums) and rest == 0:
                return 1

            if i == len(nums):
                return 0
            
            cur = nums[i]
            return helper(i+1, rest + cur) + helper(i+1, rest - cur)
        
        return helper(0, target)