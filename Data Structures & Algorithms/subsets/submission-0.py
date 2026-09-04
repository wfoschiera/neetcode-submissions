class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        subset, cur_set = [], []
        self.helper(0, nums, cur_set, subset)
        return subset

    def helper(self, idx, nums, cur_set, subset):
        # if idx (the depth of the tree) >= qtd_nums, 
        # it reaches the end and return
        if idx >= len(nums):
            subset.append(cur_set.copy())
            return
        
        # left branch, include nums[idx]
        cur_set.append(nums[idx])
        self.helper(idx + 1, nums, cur_set, subset)
        # removes nums[idx]. right branch don't include
        cur_set.pop()

        self.helper(idx + 1, nums, cur_set, subset)

        