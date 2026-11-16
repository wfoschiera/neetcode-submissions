class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 1
        while i < len(prices):
            curr = prices[i]
            prev = prices[i - 1]
            if curr > prev:
                profit += (curr - prev)
            i += 1
        return profit

