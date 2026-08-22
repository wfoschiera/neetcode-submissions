class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)

        nums = []
        i = j = 0
        while len(nums) <= total_len // 2:
            if i >= len(nums1):
                nums += nums2
                break
            elif j >= len(nums2):
                nums += nums1
                break
            elif nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                nums.append(nums2[j])
                j += 1

        if total_len % 2 == 0:
            return (nums[-2] + nums[-1]) / 2
        return nums[-1]