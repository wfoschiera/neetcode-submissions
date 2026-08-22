# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return True
            elif node.left is None and node.right is not None:
                return node.val < node.right.val
            elif node.right is None and node.left is not None:
                return node.val > node.left.val
            elif node.left is None and node.right is None:
                return True
            return node.left.val < node.val < node.right.val

        return dfs(root) and dfs(root.left) and dfs(root.right)
