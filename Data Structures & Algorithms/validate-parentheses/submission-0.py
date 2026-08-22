class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        closes = {"(":")", "[": "]", "{": "}"}
        for char in s:
            if char in ["(", "[", "{"]:
                opens.append(char)
            else:
                if char != closes[opens.pop()]:
                    return False
        return True