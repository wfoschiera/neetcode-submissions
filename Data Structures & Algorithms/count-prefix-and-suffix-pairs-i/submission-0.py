class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i, word in enumerate(words):
            p_size = len(word)
            for j, other in enumerate(words):
                if i >= j:
                    continue
                if len(other) >= p_size:
                    print(i,j)
                    print(other[:p_size] == word)
                    print(other[-p_size:] == word)
                    print()
                    if other[:p_size] == word and other[-p_size:] == word:
                        count += 1
        return count