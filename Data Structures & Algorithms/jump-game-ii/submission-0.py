class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        steps = 0
        while r < len(nums) - 1:
            fartest = 0
            for i in range(l, r + 1):
                fartest = max(fartest, nums[i] + i)
            l = r + 1
            r = fartest
            steps += 1

        return steps
