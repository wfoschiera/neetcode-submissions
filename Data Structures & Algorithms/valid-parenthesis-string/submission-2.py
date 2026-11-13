class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []

        for i, char in enumerate(s):
            
            match char:
                case "(":
                    left.append(i)
                case "*":
                    star.append(i)
                case ")":
                    if len(left) > 0:
                        left.pop()
                    elif len(star) > 0:
                        star.pop()
                    else:
                        return False
        
        while left and star:
            if left.pop() > star.pop():
                break

        return len(left) == 0