class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [3,4,5,6], target = 7

        indices = {}
        for i, num in enumerate(nums):
            indices[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        return []
