class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n == 0:
            return 1
    
        for i in range(abs(n)):
            ans *= x
        if n > 0:
            return ans
        else:
            return 1 / ans