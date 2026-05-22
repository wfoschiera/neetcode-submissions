class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_n = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
                if cur > max_n:
                    max_n = cur
            else:
                cur = 0

        return max_n
        
    def find_max_consecutive_ones_optimized(nums: list[int]) -> int:
        max_n = cur = 0
        for num in nums:
            cur = cur + 1 if num else 0
            max_n = max(max_n, cur)
   
        return max_n