class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        closes = {"(":")", "[": "]", "{": "}"}
        if len(s) < 2 or len(s) % 2 == 1:
            return False
        for char in s:
            if char in ["(", "[", "{"]:
                opens.append(char)
            else:
                if char != closes[opens.pop()]:
                    return False
        return True