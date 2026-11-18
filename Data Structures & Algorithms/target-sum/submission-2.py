from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def helper(i, rest):
            if i == len(nums) and rest == 0:
                print(i, rest)
                return 1

            if i == len(nums):
                return 0
            
            res = 0
            cur = nums[i]
            res += helper(i+1, rest + cur)
            res += helper(i+1, rest - cur)
            return res
        
        return helper(0, target)