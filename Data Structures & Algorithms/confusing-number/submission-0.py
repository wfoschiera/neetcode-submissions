class Solution:
    def confusingNumber(self, n: int) -> bool:
        for num in str(n):
            if num in (2, 3, 4, 5, 7):
                return False
        return True