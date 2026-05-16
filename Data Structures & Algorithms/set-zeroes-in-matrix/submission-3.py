class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        to_zero = []
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == 0:
                    to_zero.append((i,j))
        print(to_zero)   
        for row, _ in to_zero:
            print("row: ", row)
            matrix[row] = len(matrix[0]) * [0]
        print(matrix)
        for _, col in to_zero:
            for k, _ in enumerate(matrix):
                matrix[k][col] = 0
        
        # return matrix