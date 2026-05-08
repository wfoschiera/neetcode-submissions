class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_to_blank = []
        col_to_blank = []
        if len(matrix) == 0:
            return []
        for row, row_list in enumerate(matrix):
            for col, value in enumerate(row_list):
                if value == 0:
                    row_to_blank.append(row)
                    col_to_blank.append(col)
        print(row_to_blank)
        print(col_to_blank)
        for row in row_to_blank:
            matrix[row] = [0] * len(matrix[row])
        
        for col in col_to_blank:
            for row_n, row_v in enumerate(matrix):
                matrix[row_n][col] = 0

