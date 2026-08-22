import string 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [s for s in s.lower() if s in string.ascii_lowercase]
        return s == s[::-1]
        