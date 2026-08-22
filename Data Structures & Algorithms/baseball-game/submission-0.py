class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i, op in enumerate(operations):
            match op:
                case str(op) if op.isdigit():
                    scores.append(int(op))
                case '+':
                    lower = max(i-2, 0)
                    scores.append(sum(scores[lower:i]))
                case 'D':
                    new_score = scores[-1] * 2
                    scores.append(new_score)
                case 'C':
                    scores.pop()
        return sum(scores)
