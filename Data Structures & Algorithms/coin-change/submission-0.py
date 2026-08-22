class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or not amount:
            return 0
        
        idx = len(coins) - 1
        coin = coins[idx]
        res = []
        while amount > 0:
            if amount >= coin:
                amount -= coin
                res.append(coin)
            else:
                if idx > 0:
                    idx -= 1
                else:
                    return -1
                coin = coins[idx]

        return len(res)