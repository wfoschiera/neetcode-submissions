class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        OFFSET = 64
        while columnNumber > 26:
            columnNumber, char_ord = divmod(columnNumber, 26)
            char_ord += OFFSET
            res += chr(char_ord)
        res += chr(columnNumber + OFFSET)
        return "".join(reversed(res))
