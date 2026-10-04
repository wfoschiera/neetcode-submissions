class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, value, ocean):

            if min(r,c) < 0 or c >= COLS or r >= ROWS or (r,c) in ocean or heights[r][c] < value:
                return
            
            ocean.add((r,c))

            dfs(r+1, c, heights[r][c], ocean)
            dfs(r-1, c, heights[r][c], ocean)
            dfs(r, c+1, heights[r][c], ocean)
            dfs(r, c-1, heights[r][c], ocean)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r, c, heights[r][c], pacific)
                if r == ROWS - 1 or c == COLS - 1:
                    dfs(r, c, heights[r][c], atlantic)
        
        boths = [[r,c] for r,c in pacific if (r,c) in atlantic]
        return boths