class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, value, ocean):
            if min(r, c) < 0 or c >= COLS or r >= ROWS or (r, c) in ocean or heights[r][c] < value:
                return

            ocean.add((r, c))

            dfs(r + 1, c, heights[r][c], ocean)
            dfs(r - 1, c, heights[r][c], ocean)
            dfs(r, c + 1, heights[r][c], ocean)
            dfs(r, c - 1, heights[r][c], ocean)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)

        return [[r, c] for r, c in pacific if (r, c) in atlantic]
