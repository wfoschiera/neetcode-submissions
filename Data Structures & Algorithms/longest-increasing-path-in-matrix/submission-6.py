from functools import cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        @cache
        def dfs(r, c):
            res = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if min(nr, nc) >= 0 and nr < ROWS and nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            return res

        max_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_count = max(max_count, dfs(r, c))
        return max_count
