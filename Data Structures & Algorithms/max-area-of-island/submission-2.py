class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands_size = [0]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, size):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            size = 1
            grid[r][c] = 0

            size += dfs(r + 1, c, size)
            size += dfs(r - 1, c, size)
            size += dfs(r, c + 1, size)
            size += dfs(r, c - 1, size)
            return size

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    islands_size.append(dfs(r, c, 0))
        return max(islands_size)
