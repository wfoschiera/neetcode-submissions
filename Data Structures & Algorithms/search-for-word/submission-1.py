class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        word_len = len(word) - 1

        def dfs(r, c, idx, seen):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in seen
                or idx > word_len
                or board[r][c] != word[idx]
            ):
                return False
            if idx == word_len:
                return board[r][c] == word[idx]
            seen.add((r, c))
            idx += 1

            res = (
                dfs(r + 1, c, idx, seen)
                or dfs(r - 1, c, idx, seen)
                or dfs(r, c + 1, idx, seen)
                or dfs(r, c - 1, idx, seen)
            )
            seen.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True
        return False
