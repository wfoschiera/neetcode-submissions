class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = words
        cols = []
        for r in range(len(words)):
            
            for c in range(len(words[r])):
                if c >= len(words) \
                or r >= len(words[c]) \
                or words[c][r] != words[r][c]:
                    return False
        return True