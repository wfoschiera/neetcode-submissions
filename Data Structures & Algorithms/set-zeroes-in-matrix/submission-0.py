class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_to_blank = None
        col_to_blank = None
        if len(matrix) == 0:
            return []
        for row, row_list in enumerate(matrix):
            for col, value in enumerate(row_list):
                if value == 0:
                    row_to_blank = row
                    col_to_blank = col
                    break
        for row, row_list in enumerate(matrix):
            if row == row_to_blank:
                matrix[row] = [0]*len(row_list)
            for col, value in enumerate(row_list):
                if col != col_to_blank:
                    continue
                matrix[row][col] = 0
