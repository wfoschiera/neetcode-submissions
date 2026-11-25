class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        OFFSET = 64
        while columnNumber > 26:
            columnNumber, char_ord = divmod(columnNumber, 26)
            char_ord += OFFSET
            res.append(chr(char_ord))
        res.append(chr(columnNumber + OFFSET))
        res = "".join(res[::-1])
        return res
