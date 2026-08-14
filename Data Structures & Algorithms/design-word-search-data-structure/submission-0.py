class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]        
        curr.word = True
    
    def dfs(self, node: TrieNode, word_rest: str) -> bool:
        if not word_rest:
            return node.word
        c = word_rest[0]
        if c != ".":
            if c in node.children:
                return self.dfs(node.children[c], word_rest[1:])
            return False
        else:
            for child in node.children.values():
                if self.dfs(child, word_rest[1:]):
                    return True
            return False

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)