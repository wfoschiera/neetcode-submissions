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
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = 1
        power = abs(n)

        while power:
            if power & 1:
                res *= x

            # since >>= drops the last bit, we can ignore if n is even or odd
            power >>= 1
            x *= x
            
        return res if n > 0 else 1 / res
