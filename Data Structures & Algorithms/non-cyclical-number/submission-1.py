class Solution:
    def isHappy(self, n: int) -> bool:
        def square_digits(n: int) -> int:
            res = 0
            for i in str(n):
                res += int(i) ** 2

            return res
        
        seen = set()
        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = square_digits(n)
            
            
             
