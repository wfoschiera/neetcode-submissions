class Solution:
    # def partitionLabels(self, s: str) -> List[int]:
    # last_seen = {char: idx for idx, char in enumerate(s)}

    # res = []
    # size = end = 0
    # for i, char in enumerate(s):
    #     size += 1
    #     end = max(end, last_seen[char])

    #     if i == end:
    #         res.append(size)
    #         size = 0

    # return res

    def partitionLabels(self, s: str) -> List[int]:
        spans = {}
        for i, c in enumerate(s):
            if c in spans:
                spans[c][1] = i
            else:
                spans[c] = [i, i]
        merged = []
        for a, b in spans.values():  # at most 26 ranges
            if merged and a <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], b)
            else:
                merged.append([a, b])
        return [b - a + 1 for a, b in merged]
