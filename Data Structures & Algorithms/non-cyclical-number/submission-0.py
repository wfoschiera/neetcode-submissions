class Solution:
    def isHappy(self, n: int) -> bool:
        def square_digits(n: int) -> int:
            res = 0
            for i in str(n):
                res += int(i) ** 2

            return res
        
        seen = set()
        while True:
            digit = square_digits(n)
            if digit == 1:
                return True
            if digit in seen:
                return False
            seen.add(digit)
            
             
