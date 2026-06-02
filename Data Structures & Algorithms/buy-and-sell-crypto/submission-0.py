class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, buy in enumerate(prices):
            for j, sell in enumerate(prices):
                if j <= i:
                    continue
                max_profit = max(max_profit, sell-buy)
        return max_profit