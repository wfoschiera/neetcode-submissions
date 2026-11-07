from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        patterns = defaultdict(list)
        
        words = set(wordList)
        for word in words:
            for i in range(len(word)):
                new_pat = word[:i] + "*" + word[i+1:]
                patterns[new_pat].append(word)
        
        q = deque([(beginWord, 1)])
        while q:
            cur, dist = q.popleft()
            if cur == endWord:
                return dist
            
            for i in range(len(cur)):
                pat = cur[:i] + "*" + cur[i+1:]
                for nxt in patterns[pat]:
                    if nxt in words:
                        words.remove(nxt)
                        q.append((nxt, dist+1))
            
        return 0