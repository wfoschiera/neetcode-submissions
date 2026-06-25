class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for l in range(len(s)):
            for r in range(l, len(s)):
                char = s[l:r+1]
                reversed = "".join(char[::-1])
                if char == reversed:
                    count += 1
        return count