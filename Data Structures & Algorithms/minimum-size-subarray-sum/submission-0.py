class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        l = 0 
        subarray_sum = 0

        for r in range(len(nums)):
            subarray_sum += nums[r]
            
            while subarray_sum >= target:
                min_len = min(min_len, r - l + 1)
                subarray_sum -= nums[l]
                l += 1
        return min_len if min_len != len(nums) + 1 else 0
            