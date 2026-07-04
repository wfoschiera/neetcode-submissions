class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        highest_not_seen = 1
        for num in nums:
            seen.add(num)
        while highest_not_seen in seen:
            highest_not_seen += 1
                
        return highest_not_seen
