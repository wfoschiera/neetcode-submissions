from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # @cache
        # def dp(i, can_buy):
        #     if i >= len(prices):
        #         return 0

        #     cooldown = dp(i + 1, can_buy)
        #     if can_buy:
        #         buy = dp(i + 1, False) - prices[i]
        #         return max(buy, cooldown)
        #     else:
        #         sell = dp(i + 2, True) + prices[i]
        #         return max(sell, cooldown)

        # return dp(0, True)

        dp = {}

        def dfs(i, can_buy):
            if i >= len(prices):
                return 0
            if (i, can_buy) in dp:
                return dp[(i, can_buy)]
            
            cooldown = dfs(i + 1, can_buy)
            if can_buy:
                buy = dfs(i + 1, False) - prices[i]
                dp[(i, can_buy)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, can_buy)] = max(sell, cooldown)

            return dp[(i, can_buy)]
        
        return dfs(0, True)