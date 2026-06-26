class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min_v = nums[0]
        # for i in nums:
        #     min_v = min(min_v, i)
        # return min_v

        # cut
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
            
        return nums[l]
