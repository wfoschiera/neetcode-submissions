class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i >= j:
                    continue
                if nums[i] == nums[j]:
                    res.append((i,j))
        return len(res)