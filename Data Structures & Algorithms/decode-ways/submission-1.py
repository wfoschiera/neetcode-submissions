from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def dfs(i: int):
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            ans = dfs(i + 1)

            if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
                ans += dfs(i + 2)

            return ans

        return dfs(0)

