class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # if nums[0] != 0:
        #     return 0
    
        # for i, n in enumerate(nums):
        #     if i == len(nums) - 1:
        #         return n + 1
        #     if n + 1 != nums[n+1]:
        #         return n+1

        n = len(nums)  # in python len of a list is O(1)
        # res start with the highest value possible
        # p.e.: if nums = [0,1,2], than res = 3. If every
        # num in nums is sequential, than the missed will be 3
        res = n
        # if we sum(nums) and subtract from the sum from [0,n]
        # the result will be the missing number
        for i in range(n):
            # but we can do both sums in a single running
            # summing the subtract of i minus nums[i]
            res += i - nums[i]

        return res

