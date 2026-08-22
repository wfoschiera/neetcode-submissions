class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        longest = 0
        count = 0
        for i in s:
            if i not in visited:
                count += 1
            else:
                count = 1
                visited = set()
            visited.add(i)
            longest = max(longest, count)
        return longest