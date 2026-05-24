class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        closes = {"(":")", "[": "]", "{": "}"}
        
        if len(s) % 2 == 1:
            return False
        
        for char in s:
            if char in ["(", "[", "{"]:
                opens.append(char)
            else:
                try:
                    if closes[opens.pop()] != char:
                        return False

                except IndexError:
                    return False

        return True if not opens else False