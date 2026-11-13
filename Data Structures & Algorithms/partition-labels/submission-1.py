class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sub_hash = {char: idx for idx, char in enumerate(s)}

        res = []
        size = end = 0
        for i, char in enumerate(s):
            size += 1
            end = max(end, sub_hash[char])

            if i == end:
                res.append(size)
                size = 0
        
        return res