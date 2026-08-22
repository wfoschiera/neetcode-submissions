class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        res = []
        for token in tokens:
            match token:
                case "-":
                    res = [res[0] - res[1]]
                case "+":
                    res = [res[0] + res[1]]
                case "*":
                    res = [res[0] * res[1]]
                case "/":
                    res = [res[0] / res[1]]
                case _:
                    res.append(int(token))
        return res[0]