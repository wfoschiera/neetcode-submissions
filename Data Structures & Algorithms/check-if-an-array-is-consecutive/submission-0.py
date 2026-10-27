class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        check_1 = max(nums) - min(nums) == len(nums) - 1
        check_2 = len(set(nums)) == len(nums)
        return check_1 and check_2