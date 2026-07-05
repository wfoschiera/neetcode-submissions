# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def dfs(node):
            depth = 0
            if node is None:
                return depth
            else:
                depth += 1
                ld = dfs(node.left)
                rd = dfs(node.right)

            max_d = max(ld, rd)
            return max_d + depth
        d = dfs(root)
        return d