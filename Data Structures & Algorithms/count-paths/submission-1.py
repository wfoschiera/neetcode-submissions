from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        seen = set()

        @lru_cache
        def dfs(r, c):
            paths = 0
            
            if r == ROWS-1 and c == COLS-1:
                return 1

            if r == ROWS -1 :
                return dfs(r, c+1)

            if c == COLS -1:
                return dfs(r+1, c)

            paths = dfs(r, c+1) + dfs(r+1, c)
            return paths

        return dfs(0, 0)