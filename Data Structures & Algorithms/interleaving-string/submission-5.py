from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dfs(i, j):
            k = i + j
            match_s1, match_s2 = False, False

            if k == len(s3):
                return True

            if i < len(s1) and s1[i] == s3[k]:
                match_s1 = True

            if j < len(s2) and s2[j] == s3[k]:
                match_s2 = True

            return (match_s1 and dfs(i+1, j) or match_s2 and dfs(i, j+1))
        return dfs(0, 0)
