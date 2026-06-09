class Solution:
    def idx_to_pos(self, idx, col_len):
        row = idx // col_len
        col = idx % col_len
        return row, col

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        low = 0
        high = (rows * cols) - 1

        while low <= high:
            mid = (low + high) // 2
            row, col = self.idx_to_pos(mid, cols)
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False