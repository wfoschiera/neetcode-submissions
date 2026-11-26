class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # if ABC comes before AB, p.e, return ""
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            # compare both words, char by char
            for j in range(min_len):
                if w1[j] != w2[j]:
                    # and adds to adj_list if the chars differ from each other
                    adj[w1[j]].add(w2[j])
                    break

        path = {}
        res = []

        def dfs(letter):
            if letter in path:
                return path[letter]
            path[letter] = True
            for neighbor in adj[letter]:
                if dfs(neighbor):
                    return True
            path[letter] = False
            res.append(letter)
            return False

        for letter in list(adj.keys()):
            if dfs(letter):
                return ""
        return "".join(res[::-1])