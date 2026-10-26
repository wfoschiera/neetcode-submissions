class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            total -= num
            if left == total:
                return i
            left += num
        return -1