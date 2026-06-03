class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1  # nums1 valid
        j = n-1  # nums2
        k = m + n - 1  # in place nums1
        
        while k >= 0:
            print("i: ", i, "j: ", j)
            if i >= 0 and j >= 0:
                if nums1[i] >= nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
