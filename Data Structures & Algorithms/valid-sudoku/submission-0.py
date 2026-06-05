class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        cols = defaultdict(list)
        boxes = defaultdict(list)
        
        for i in range(len(board)):
            row_filtered = [x for x in board[i] if x != '.']
            if len(row_filtered) != len(set(row_filtered)):
                return False
            for j in range(len(board)):
                if board[i][j] == '.': continue
                cols[j].append(board[i][j])
                ind_row = i // 3
                ind_col = j // 3
                boxes[(ind_row, ind_col)].append(board[i][j])

        for col in cols.values():
            if len(col) != len(set(col)):
                return False
        
        for subbox in boxes.values():
            if len(subbox) != len(set(subbox)):
                return False

        return True