class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)

    def helper(self, i, nums):
        if i == len(nums):
            return [[]]
        
        seen = set()
        res_perms = []
        perms = self.helper(i + 1, nums)

        for p in perms:
            for j in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(j, nums[i])
                t = tuple(p_copy)
                if t not in seen:
                    res_perms.append(p_copy)
                    seen.add(t)
                    
        return res_perms