from functools import cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def min_cost(i):
            if i >= len(cost):
                return 0

            return cost[i] + min(min_cost(i + 1), min_cost(i + 2))

        return min(min_cost(0), min_cost(1))