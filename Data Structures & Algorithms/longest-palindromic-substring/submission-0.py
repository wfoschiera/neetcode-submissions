class Solution:
    def longestPalindrome(self, s: str) -> str:
        def aux(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        longest = ""
        for i in range(len(s)):
            l, r = i, i
            pal1 = aux(l, r, s)
            longest = pal1 if len(pal1) > len(longest) else longest
            l, r = i, i + 1
            pal2 = aux(l, r, s)
            longest = pal2 if len(pal2) > len(longest) else longest
        return longest
