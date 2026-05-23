class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i, op in enumerate(operations):
            match op:

                case '+':
                    score = scores[-1] + scores[-2]
                    scores.append(score)
                case 'D':
                    new_score = scores[-1] * 2
                    scores.append(new_score)
                case 'C':
                    scores.pop()
                case _:
                    scores.append(int(op))
            print(scores)
        return sum(scores)
