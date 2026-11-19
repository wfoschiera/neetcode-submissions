from functools import cache 


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        @cache
        def dfs(i, string):
            if string == t:
                return 1
            if i == len(s):
                return 0

            return dfs(i+1, string + s[i]) + dfs(i+1, string)

        return dfs(0, "")
        