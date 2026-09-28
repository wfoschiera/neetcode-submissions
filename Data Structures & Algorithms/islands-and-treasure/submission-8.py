from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        q = deque()

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == -1 or (r, c) in seen:
                return
            seen.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    seen.add((r, c))

        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            distance += 1
