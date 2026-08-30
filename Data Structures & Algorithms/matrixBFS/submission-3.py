from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        NEIGHBOURS = [(0,1), (0,-1), (1,0), (-1,0)]
        visit = set()
        queue = deque()
        lenght = 0

        def out_of_bounds(r, c):
            if (min(r,c) < 0 or
                r == ROWS or
                c == COLS or
                (r,c) in visit or
                grid[r][c] == 1
            ):
                return True
            return False

        if grid[0][0] == 0:
            queue.append((0,0))
            visit.add((0,0))


        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return lenght

                for dr, dc in NEIGHBOURS:
                    R, C = r+dr, c+dc
                    if out_of_bounds(R,C):
                        continue
                    queue.append((R,C))
                    visit.add((R,C))
            lenght += 1
        return -1