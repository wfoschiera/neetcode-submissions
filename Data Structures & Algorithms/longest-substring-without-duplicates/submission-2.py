class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        
        longest = 0
        for l in range(len(s)):
            r = l + 1
            visited.add(s[l])
            while r < len(s) and s[r] not in visited:
                visited.add(s[r])
                r += 1
            
            visited = set()
            longest = max(longest, (r-l))
            
        return longest