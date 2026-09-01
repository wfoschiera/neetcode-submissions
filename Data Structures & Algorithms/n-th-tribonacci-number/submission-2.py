class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        
        if n <= 2:
            return dp[n]
        
        i = 2
        while i < n:
            temp = dp[2]
            dp[2] = dp[0] + dp[1] + dp[2]
            dp[0], dp[1] = dp[1], temp
            i += 1
        return dp[2]