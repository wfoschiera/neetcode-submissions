
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)

        m = max(c.values())

        inv = {v: k for k, v in c.items()}
        return inv[m]
        
