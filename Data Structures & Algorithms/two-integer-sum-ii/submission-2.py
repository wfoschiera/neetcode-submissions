class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sum_map = {num: (target - num, i) for i, num in enumerate(numbers)}
        # for i, num in enumerate(numbers):
        #     if target - num in sum_map:
        #         index_i = sum_map[num][1]
        #         index_j = sum_map[target - num][1]
        #         if index_i < index_j:
        #             return [index_i + 1, index_j + 1]
        # Time complexity: O(n)
        # Space complexity O(n)  -> wrong

        # Using two pointers

        l = 0
        r = len(numbers) - 1
        while l < r:
            _sum = numbers[l] + numbers[r]
            if _sum == target:
                return [l+1, r+1]
            
            elif _sum < target:
                l += 1
            elif _sum > target:
                r -= 1
        return False