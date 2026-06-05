class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                cel = board[i][j]
                if cel == ".":
                    continue

                ind_row = i // 3
                ind_col = j // 3

                if cel in cols[j] or cel in rows[i]:
                    return False
                if cel in boxes[ind_row, ind_col]:
                    return False

                cols[j].add(cel)
                rows[i].add(cel)
                boxes[(ind_row, ind_col)].add(cel)

        return True
