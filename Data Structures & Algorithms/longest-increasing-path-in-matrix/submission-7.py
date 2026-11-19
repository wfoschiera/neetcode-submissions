from functools import cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dr_dc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @cache
        def dfs(r, c):
            res = 1
            for dr, dc in dr_dc:
                nr, nc = r + dr, c + dc
                if min(nr, nc) >= 0 and nr < ROWS and nc < COLS and matrix[r][c] < matrix[nr][nc]:
                    res = max(res, 1 + dfs(nr, nc))
            return res

        max_seq = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_seq = max(max_seq, dfs(r, c))

        return max_seq
