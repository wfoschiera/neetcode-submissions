class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ans = 1
        # if n == 0:
        #     return 1
    
        # for i in range(abs(n)):
        #     ans *= x
        # if n > 0:
        #     return ans
        # else:
        #     return 1 / ans

        # Using Binary Exponentiation (new for me 17/06/26)
        orig_n = n
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = 1
        n = abs(n)
        while n > 1:
            if n % 2 == 0:
                n /= 2
                x *= x
            
            else:
                res *= x
                n -= 1
        res *= x
        return res if orig_n > 0 else 1 / res
