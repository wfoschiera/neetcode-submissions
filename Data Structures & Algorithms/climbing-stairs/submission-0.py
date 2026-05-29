class Solution:

    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        steps = 0
        if n-1 not in self.cache:
            self.cache[n-1] = self.climbStairs(n-1)

        steps += self.cache[n-1]
            
        if n >= 2:
            if n-2 not in self.cache:
                self.cache[n-2] = self.climbStairs(n-2)
            steps += self.cache[n-2]
        
        return steps