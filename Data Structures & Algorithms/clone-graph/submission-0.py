"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = dict()
        
        if node is None:
            return None
        
        def dfs(curr):
            if curr in seen:
                return seen[curr]

            copy = Node(curr.val)
            seen[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        dfs(node)
        
        return seen[node]
            