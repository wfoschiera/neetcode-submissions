class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}

        while pq:
            time, r, c = heapq.heappop(pq)
            if r == ROWS - 1 and c == COLS - 1:
                return time
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(pq, (max(time, grid[nr][nc]), nr, nc))