class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax = globMin = nums[0]
        curMax = curMin = 0
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        # If globMax <= 0, all values are non-positive → answer is globMax (the largest single element).
        return max(globMax, total - globMin) if globMax > 0 else globMax