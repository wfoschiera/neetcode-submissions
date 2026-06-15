class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for num in nums:
            count[num] += 1
            
        
        i = 0
        for j, qty in enumerate(count):
            nums[i:i+qty] = [j] * qty
            i += qty
        