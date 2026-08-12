class Solution:
    def countBits(self, n: int) -> List[int]:
        # res = []
        # for i in range(n+1):
        #     num = bin(i).split('b')[1]
        #     res.append(num.count('1'))

        # return res

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
            print(i, dp[i])
        return dp