from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = defaultdict(set)
        self.visited = set()

    def addEdge(self, src: int, dst: int) -> None:
        self.nodes[src].add(dst)    

    def removeEdge(self, src: int, dst: int) -> bool:
        origin_node = self.nodes.get(src)
        if origin_node is None or dst not in origin_node:
            return False
        self.nodes[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        self.visited = set()
        return self.dfs(src, dst)

    def dfs(self, src: int, dst: int):
        if src == dst:
            return True
        adj_nodes = self.nodes.get(src)
        if adj_nodes is None:
            return False
        for node in adj_nodes:
            if node in self.visited:
                continue
            self.visited.add(node)
            if self.dfs(node, dst):
                return True
        return False
