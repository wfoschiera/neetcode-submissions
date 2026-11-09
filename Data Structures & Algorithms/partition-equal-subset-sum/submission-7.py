from functools import lru_cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2 == 1:
            return False

        target = _sum // 2

        @lru_cache(None)
        def dfs(i, cur_sum):
            if cur_sum == target:
                return True
            if i == len(nums) or cur_sum > target:
                return False


            if dfs(i + 1, cur_sum + nums[i]) is True:
                return True
            if dfs(i + 1, cur_sum) is True:
                return True
            return False

        return dfs(0, 0)
