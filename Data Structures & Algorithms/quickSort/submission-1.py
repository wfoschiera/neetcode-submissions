# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(s, e):
            l = s

            if e - s + 1 <= 1:
                return pairs

            for i in range(s, e):
                if pairs[i].key < pairs[e].key:  # pairs[e] => pivot
                    pairs[l], pairs[i] = pairs[i], pairs[l]
                    l += 1
            # move pivot -> lower < pivot < higher
            pairs[e], pairs[l] = pairs[l], pairs[e]

            sort(s, l - 1)  # without pivot
            sort(l + 1, e)  # without pivot

        sort(0, len(pairs) - 1)
        return pairs
