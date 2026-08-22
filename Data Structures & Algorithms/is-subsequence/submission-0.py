from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        count_t = Counter(t)
        print(count_t)
        for letter in s:
            if letter not in count_t or count_t[letter] <=0:
                return False
            count_t[letter] -= 1
            
        return True
        