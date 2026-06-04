from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = defaultdict(list)
        for word in strs:
            key = tuple(sorted(list(word)))
            sorted_words[key].append(word)
        print(sorted_words)
        return list(sorted_words.values())