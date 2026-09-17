class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)
        
    def helper(self, i, nums):
        if i == len(nums):
            return [[]]
        
        res = []
        perms = self.helper(i + 1, nums)
        print(f"\n{i=}, {perms=}")
        for p in perms:
            print(f"{p=}")
            for j in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(j, nums[i])
                print(f"{pCopy=}")
                res.append(pCopy)
            print(f"final local p: {pCopy}")
        return res