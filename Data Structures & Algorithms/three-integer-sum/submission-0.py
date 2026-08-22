class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorted(nums)
        ans = []
        for i, v in enumerate(nums):
            for j, w in enumerate(nums):
                for k, x in enumerate(nums):
                    if j <= i or k <= j:
                        continue
                    if v + w + x == 0:
                        triplet = sorted([v, w, x])
                        if triplet in ans:
                            continue
                        ans.append(triplet)
        return ans