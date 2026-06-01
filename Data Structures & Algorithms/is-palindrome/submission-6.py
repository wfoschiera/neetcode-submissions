import string 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_nums = "0123456789"
        valid_chars = string.ascii_lowercase
        valid_letters = valid_nums + valid_chars
        s = [s for s in s.lower() if s in valid_letters]
        return s == s[::-1]
        