class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorted(nums)
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    # if j <= i or k <= j:
                    #     continue
                    x, y, z = nums[i], nums[j], nums[k]
                    if x + y + z == 0:
                        triplet = tuple(sorted([x, y, z]))
                        if triplet in ans:
                            continue
                        ans.add(triplet)
        return [list(a) for a in ans]