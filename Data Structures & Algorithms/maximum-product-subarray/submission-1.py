class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = 1
        res = nums[0]

        for num in nums:
            tmp = max_prod * num
            max_prod = max(max_prod* num, min_prod * num, num)
            min_prod = min(tmp, num * min_prod, num)
            res = max(res, max_prod)
        return res  