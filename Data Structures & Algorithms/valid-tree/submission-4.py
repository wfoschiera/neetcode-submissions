from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visit, cycle = set(), set()
        adj_list = defaultdict(set)
        for node1, node2 in edges:
            adj_list[node1].add(node2)
            adj_list[node2].add(node1)

        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)

            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                if dfs(neighbour, node) == False:
                    return False

            return True

        if dfs(0, -1) == False:
            return False
        return len(visit) == n
