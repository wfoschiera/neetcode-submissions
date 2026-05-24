class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        closes = {"(":")", "[": "]", "{": "}"}
        if len(s) % 2 == 1:
            return False
        for char in s:
            if char in ["(", "[", "{"]:
                opens.append(char)
            if char in ["]", ")", "}"]:
                try:
                    if closes[opens.pop()] != char:
                        return False

                except IndexError:
                    return False
        if len(opens) > 0:
            return False
        return True