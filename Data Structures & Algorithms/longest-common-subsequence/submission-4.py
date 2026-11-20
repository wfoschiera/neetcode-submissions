from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        
        @cache
        def helper(i, j):
            if i > len(text1) - 1 or j > len(text2) - 1:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + helper(i+1, j+1)

            return max(helper(i+1, j), helper(i, j+1))
        
        return helper(0, 0)