class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower_k = 1
        upper_k = max(piles)
        
        res = upper_k
        while lower_k <= upper_k:
            total_time = 0

            k = (lower_k + upper_k) // 2

            for pile in piles:
                time_to_eat = math.ceil(pile/k)
                total_time += time_to_eat 
                
            if total_time <= h:
                res = k
                upper_k = k - 1
            else:
               lower_k = k + 1

        return res
        