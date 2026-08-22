class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        shape = len(image), len(image[0])
        init_color = image[sr][sc]
        grid = image
        def dfs(r, c, visit, shape, color):
            ROWS, COLS = shape
            # start with conditions
            # check if r and c are inside grid dimension
            # and if grid[r][c] has the same initial color
            # or was already visited
            if (
                min(r, c) < 0
                or (r == ROWS or c == COLS)
                or (grid[r][c] != init_color)
                or (r, c) in visit
            ):
                return 

            grid[r][c] = color
            visit.add((r, c))

            dfs(r + 1, c, visit, shape, color)
            dfs(r - 1, c, visit, shape, color)
            dfs(r, c + 1, visit, shape, color)
            dfs(r, c - 1, visit, shape, color)
            return 

        dfs(sr, sc, set(), shape, color)
        return grid
