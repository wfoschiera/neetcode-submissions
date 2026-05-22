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
            