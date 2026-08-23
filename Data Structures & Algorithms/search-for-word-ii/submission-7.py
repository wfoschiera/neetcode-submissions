class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res = set()
        # path = set()
        # insert every word in the Trie
        root = TrieNode()
        for w in words:
            root.insert(w)

        # the dfs compares each branch with and existing word in the Trie simultaniously
        def dfs(r, c, node, word):
            if (
                min(r,c) < 0 or 
                r == ROWS or 
                c == COLS or 
                # (r, c) in path or 
            board[r][c] not in node.children):
                return 

            # path.add((r, c))
            

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEndOfWord:
                res.add(word)

            board[r][c] = "*"
            found = (
                dfs(r + 1, c, node, word)
                or dfs(r - 1, c, node, word)
                or dfs(r, c + 1, node, word)
                or dfs(r, c - 1, node, word)
            )
            # path.remove((r, c))
            board[r][c] = word[-1]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
