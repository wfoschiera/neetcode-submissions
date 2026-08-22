from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = Counter(s)
        l = 0
        r = 1


        while r < len(s) -1 and l < r:
            r += 1
            if (r-l+1) - max(freq.values()) > k:
                l += 1
                freq[s[l]] -= 1
        return r-l+1