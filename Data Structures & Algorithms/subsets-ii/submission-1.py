class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        subset, cur_set = [], []
        nums.sort()

        def dfs(idx):
            # reachs the end (depth) of the tree
            if idx >= len(nums):
                subset.append(cur_set.copy())
                return

            # we should divide in 2 branchs
            # 1. adds every repeated number
            cur_set.append(nums[idx])
            dfs(idx + 1)
            cur_set.pop()

            # 2. do not add ANY repeated number
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(idx + 1)

        dfs(0)
        return subset
