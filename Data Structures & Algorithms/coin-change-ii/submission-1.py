from functools import cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def helper(remaining, i):
            if remaining == 0:
                return 1
            elif remaining < 0:
                return 0
            elif i > len(coins) - 1:
                return 0
            
            b = helper(remaining, i + 1)
            remaining -= coins[i]
            a = helper(remaining, i)  

            return a + b
        return helper(amount, 0)
