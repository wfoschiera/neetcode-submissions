class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 26:
            columnNumber, char_ord = divmod(columnNumber, 26)
            char_ord += 64
            res.append(chr(char_ord))
        res.append(chr(columnNumber+64))
        res = "".join(res[::-1])
        return res