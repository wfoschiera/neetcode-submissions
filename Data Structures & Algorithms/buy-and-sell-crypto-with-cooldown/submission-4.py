from functools import cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @cache
        def dp(i, can_buy):
            if i >= len(prices):
                return 0

            cooldown = dp(i + 1, can_buy)
            if can_buy:
                buy = dp(i + 1, False) - prices[i]
                return max(buy, cooldown)
            else:
                sell = dp(i + 2, True) + prices[i]
                return max(sell, cooldown)

        return dp(0, True)
