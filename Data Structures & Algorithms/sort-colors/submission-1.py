class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = [0,0,0]
        # for num in nums:
        #     count[num] += 1
            
        
        # i = 0
        # for j, qty in enumerate(count):
        #     nums[i:i+qty] = [j] * qty
        #     i += qty
        
        # three pointer
        zero = one = two = 0
        for i, num in enumerate(nums):
            if num == 0:
                nums[two] = 2
                nums[one] = 1
                nums[zero] = 0
                two += 1
                one += 1
                zero += 1
            elif num == 1:
                nums[two] = 2
                nums[one] = 1
                two += 1
                one += 1
            else:
                nums[two] = 2
                two += 1