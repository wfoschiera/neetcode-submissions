class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        res = []
        for token in tokens:
            match token:
                case "-":
                    b, a = res.pop(), res.pop()
                    res.append(a - b)
                case "+":
                    b, a = res.pop(), res.pop()
                    res.append(a + b)
                case "*":
                    b, a = res.pop(), res.pop()
                    res.append(a * b)
                case "/":
                    b, a = res.pop(), res.pop()
                    res.append(int(a / b))
                case _:
                    res.append(int(token))
        return res[0]