class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges) + 1
        par = [i for i in range(size)]
        rank = [1] * size

        def find_par(node):
            cur = node
            while cur != par[cur]:
                par[cur] = par[par[cur]]
                cur = par[cur]
            return cur

        def union(u, v):
            pv = find_par(v)
            pu = find_par(u)

            if pu == pv:
                return False

            if rank[pv] > rank[pu]:
                pu, pv = pv, pu

            par[pv] = pu
            rank[pu] += rank[pv]
            return True

        for u, v in edges:
            if union(u, v) is False:
                return [u, v]
