class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        prices = [INF] * n
        prices[src] = 0

        for i in range(k + 1):
            tmp_prices = prices.copy()

            for s, d, p in flights:
                if prices[s] == None:
                    continue

                if prices[s] + p < tmp_prices[d]:
                    tmp_prices[d] = prices[s] + p

            prices = tmp_prices
        return prices[dst] if prices[dst] != INF else -1

