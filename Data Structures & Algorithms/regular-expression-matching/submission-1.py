from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @cache
        def dfs(i, j):
            if j == n:
                return i == m

            match_ = i < m and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < n and p[j + 1] == "*":
                res = dfs(i, j + 2) or (match_ and dfs(i + 1, j))
                return res

            if match_:
                res = dfs(i + 1, j + 1)
                return res

            return False

        return dfs(0, 0)
