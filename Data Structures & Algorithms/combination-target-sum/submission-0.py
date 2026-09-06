class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = list()
        cur_set = list()

        def dfs(cur_set, idx):
            total = sum(cur_set)
            if total == target:
                subsets.append(cur_set.copy())
                return
            if total > target:
                return
            
            for i in range(idx, len(nums)):
                cur_set.append(nums[i])
                dfs(cur_set, i)
                cur_set.pop()
        
        dfs(cur_set, 0)
        return subsets