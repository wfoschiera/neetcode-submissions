class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dups_idx = []
        seen = {}

        for i, num in enumerate(nums):
            if num in seen:
                dups_idx.append((seen[num], i))
            seen[num] = i
        
        for dup in dups_idx:
            i, j = dup
            if abs(i-j) <= k:
                return True

        return False
