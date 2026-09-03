class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr2_map = {}
        for i, num in enumerate(nums2):
            arr2_map[num] = i
        
        res = []

        for num in nums1:
            if num in arr2_map:
                res.append(arr2_map[num])
                
        return res