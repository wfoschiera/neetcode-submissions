class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i, op in enumerate(operations):
            match op:

                case '+':
                    lower = max(i-2, 0)
                    scores.append(sum(scores[lower:i]))
                case 'D':
                    new_score = scores[-1] * 2
                    scores.append(new_score)
                case 'C':
                    scores.pop()
                case _:
                    scores.append(int(op))
            print(scores)
        return sum(scores)
