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

        sortArray[left]
        sortArray[right]

        # CONQUER
        i = j = k = 0

        # compare elements of both halves
        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # remaining elements in left
        while i < left:
            arr[k] = left[i]
            i += 1
            k += 1
        # remaining elements in right 
        while i < right:
            arr[k] = right[j]
            j += 1
            k += 1

        return arr