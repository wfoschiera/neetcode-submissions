class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip(".'\/\"?!#%:@").lower().replace(" ", "")
        s = list(s)
        return s == s[::-1]
        