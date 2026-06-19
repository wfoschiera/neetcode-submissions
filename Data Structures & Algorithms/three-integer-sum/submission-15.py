class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:  # when sorted, if nums[i] > 0 => nums[l] > 0 and nums[r] > 0
                break

            if i > 0 and nums[i] == nums[i-1]:  # if next nums is equal to previous, continue. Avoid duplicates
                continue

            # two pointers right after i position
            l = i + 1
            r = len(nums) - 1

            while l < r:
                triplet = [nums[i], nums[l], nums[r]]
                s = sum(triplet)
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    ans.append(triplet)
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r -1]:
                        r -=1
                    l += 1
                    r -= 1
        return ans