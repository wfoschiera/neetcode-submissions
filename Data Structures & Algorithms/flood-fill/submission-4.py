class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        init_color = image[sr][sc]
        grid = image
        def dfs(r, c, visit):
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

            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)
            return 

        dfs(sr, sc, set())
        return grid
