class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        
        if n <= 2:
            return dp[n]
        
        i = 2
        # Since we now N, this loop can be for i in range(3, n+1)
        while i < n:
            # neetcode uses t[i % 3] to store the last value using a cyclic approach
            # t[i % 3] = sum(t)
            temp = dp[2]
            dp[2] = dp[0] + dp[1] + dp[2]
            dp[0], dp[1] = dp[1], temp
            i += 1
        return dp[2]