class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorted(nums)
        ans = set()
        for i, v in enumerate(nums):
            for j, w in enumerate(nums):
                for k, x in enumerate(nums):
                    if j <= i or k <= j:
                        continue
                    if v + w + x == 0:
                        triplet = tuple(sorted([v, w, x]))
                        if triplet in ans:
                            continue
                        ans.add(triplet)
        return [list(a) for a in ans]