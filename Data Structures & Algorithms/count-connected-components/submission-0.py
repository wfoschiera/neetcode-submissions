class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union join
        parent = [i for i in range(n)]
        rank = [1] * n  # todo mundo começa com 1

        def find(n1):
            """find the node's parent"""
            cur = n1
            while cur != parent[cur]:
                print(f"{cur=} {parent[cur]=}")
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            return cur

        def union(u, v):
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return 0

            if rank[pv] > rank[pu]:
                pu, pv = pv, pu
            
            parent[pv] = pu
            rank[pu] += rank[pv]
            return 1

        res = n
        for u, v in edges:
            res -= union(u, v)
        return res

        