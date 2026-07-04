class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # using mergeSort O(nlogn) Best/Avg/Worst
        # O(n) space
        # Stable
        
        if len(nums) <= 1:
            return nums

        # DIVIDE
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        self.sortArray(left)
        self.sortArray(right)

        # CONQUER
        i = j = k = 0

        # compare elements of both halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        # remaining elements in left
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        # remaining elements in right 
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

        return nums