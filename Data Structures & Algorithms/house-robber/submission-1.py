class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) < 1:
        #     return 0
        # return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        rob1 = rob2 = 0

        for n in nums:
            # pick one or another, avoid neighbors
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2