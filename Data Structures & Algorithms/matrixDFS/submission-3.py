class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        seen = set()
        ROWS, COLS = len(grid) - 1, len(grid[0]) - 1
        count = 0

        def dfs(r, c):
            nonlocal count

            if min(r, c) < 0 or (r, c) in seen or r > ROWS or c > COLS or grid[r][c] == 1:
                return

            seen.add((r, c))
            if r == ROWS and c == COLS:
                count += 1
                # return

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            seen.remove((r, c))

        dfs(0, 0)
        return count
