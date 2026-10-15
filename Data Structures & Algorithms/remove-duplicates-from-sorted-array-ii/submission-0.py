class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        L = 2

        for R in range(2, len(nums)):
            if nums[L - 2] != nums[R]:
                nums[L] = nums[R]
                L += 1

        return L