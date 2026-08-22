class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(n):
            num = (n >> i) & 1
            if num == 1:
                res |= (1 << (31 - i))
        return res