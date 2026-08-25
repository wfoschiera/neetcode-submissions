class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = False
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                word = True
                _len = 0
                while i >= 0 and s[i] != " ":
                    _len += 1
                    i -= 1
                return _len
        return -1