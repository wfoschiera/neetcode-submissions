from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        q = deque()
        
        if grid[0][0] != 0 or grid[ROWS-1][COLS-1] != 0:
            return -1

        q.append((0,0))
        grid[0][0] = 1

        while q:
            r, c = q.popleft()
            dist = grid[r][c]

            if r == ROWS -1 and c == COLS -1:
                return dist

            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if min(nr, nc) >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 0:
                    grid[nr][nc] = dist + 1
                    q.append((nr, nc))
            
        return -1