# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.total = float("-inf")

        def dfs(node):
            if node is None:
                return 0

            # consider only positive values
            l = max(dfs(node.left), 0)  
            r = max(dfs(node.right), 0)


            _local = node.val + l + r
            self.total = max(self.total, _local)

            return node.val + max(l, r)

        dfs(root)
        return self.total
