from functools import cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        @cache
        def dp(i, j):
            if i > j:
                return 0
            
            max_coins = 0
            for k in range(i, j + 1):
                coins = nums[i - 1] * nums[k] * nums[j + 1] + dp(i, k - 1) + dp(k + 1, j)
                max_coins = max(coins, max_coins)
            
            return max_coins

        return dp(1, len(nums) - 2)