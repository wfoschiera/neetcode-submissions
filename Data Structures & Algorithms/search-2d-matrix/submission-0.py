class Solution:
    def idx_to_pos(self, idx, row_len):
        col = 0
        row = 0
        while idx > col:
            col +=1
            row = idx // row_len
        return row, col % row_len

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0])
        idx = (row_len * col_len) - 1

        visited = set()
        while True:
            idx = idx // 2

            row, col = self.idx_to_pos(idx, row_len)
            if (row, col) in visited:
                return False
            visited.add((row, col))

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row = row // 2
                col = col // 2
            elif matrix[row][col] < target:
                row = row_len // 2
                col = col_len // 2

        return False