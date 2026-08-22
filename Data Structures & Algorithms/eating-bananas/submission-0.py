class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower_k = 1
        upper_k = max(piles)
        
        total_time = h+1
        while total_time > h:
            total_time = 0
            k = (lower_k + upper_k) // 2

            for pile in piles:
                time_to_eat = math.ceil(pile/k)
                print(time_to_eat)
                total_time += time_to_eat
            print(total_time)
            if total_time > h:
               lower_k = k + 1
                
        return k
        