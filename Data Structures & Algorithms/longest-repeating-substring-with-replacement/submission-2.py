class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1

        longest = 1
        local_lon = 1
        substitutions = k
        while l < len(s) - 2:
            if r < len(s) - 1 and s[l] == s[r]:
                local_lon += 1
                r += 1
            elif r <= len(s) - 1 and substitutions > 0:
                local_lon += 1
                r += 1
                substitutions -= 1
            else:
                local_lon = 1
                l += 1
                r = l + 1
                substitutions = k
            longest = max(longest, local_lon)

        return longest
