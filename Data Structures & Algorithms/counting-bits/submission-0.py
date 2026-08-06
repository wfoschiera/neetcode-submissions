class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            num = bin(i).split('b')[1]
            res.append(num.count('1'))

        return res