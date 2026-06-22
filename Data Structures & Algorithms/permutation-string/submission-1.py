from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        
        while r <= len(s2):
            w = s2[l:r]
            hash_map = Counter(w)
            contains = True
            for letter in s1:
                if hash_map[letter] < 1:
                    contains = False
                hash_map[letter] -= 1
            
            if contains is True:
                return True
            l += 1
            r += 1
        return False