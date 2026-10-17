class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        # tip: Avoid using [[0] * R] * C]. This will not create independent copies
        self.prefix_matrix = [[0] * self.COLS for _ in range(self.ROWS)]
        for row in range(self.ROWS):
            for col in range(self.COLS):
                cel = self.matrix[row][col]
                prev_cel = self.get_val(row, col-1)
                upper_cel = self.get_val(row-1, col)
                diag_cel = self.get_val(row-1, col-1)

                self.prefix_matrix[row][col] = cel + prev_cel + upper_cel - diag_cel

    def get_val(self, row, col):
        if min(row, col) < 0:
            return 0
        return self.prefix_matrix[row][col]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        M = self.get_val
        return (M(row2, col2) + M(row1-1, col1-1)) - (M(row1-1, col2) + M(row2, col1-1))

# [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
# [[14, 12, 10, 12, 28], [14, 12, 10, 12, 28], [14, 12, 10, 12, 28], [14, 12, 10, 12, 28], [14, 12, 10, 12, 28]]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)