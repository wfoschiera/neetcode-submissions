from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.nodes[src].add(dst)    

    def removeEdge(self, src: int, dst: int) -> bool:
        origin_node = self.nodes.get(src)
        if origin_node is None or dst not in origin_node:
            return False
        self.nodes[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src, dst, set())

    def dfs(self, src: int, dst: int, visited: set):
        if src == dst:
            return True
        visited.add(src)

        for node in self.nodes.get(src, []):
            if node in visited:
                continue
            
            if self.dfs(node, dst, visited):
                return True
        return False
