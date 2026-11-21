from functools import cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        @cache
        def dp(i, j):
            if i > j:
                return 0
            # if (i, j) in memo:
            #     return memo[(i, j)]
            
            max_coins = 0
            for k in range(i, j + 1):
                coins = nums[i - 1] * nums[k] * nums[j + 1] + dp(i, k - 1) + dp(k + 1, j)
                if coins > max_coins:
                    max_coins = coins
            
            # memo[(i, j)] = max_coins
            return max_coins

        return dp(1, len(nums) - 2)