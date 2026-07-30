class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            # Xor cancels every equal number
            res = res ^ num

        return res