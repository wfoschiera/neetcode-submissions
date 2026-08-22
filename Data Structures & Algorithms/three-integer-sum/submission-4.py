class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = []
        for i in range(len(nums) - 2):  # -2 (i and j)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                x, y, z = nums[i], nums[l], nums[r]
                s = x + y + z
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    ans.append([x, y, z])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r -1]:
                        r -=1
        return ans