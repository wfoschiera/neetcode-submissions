# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        values = []

        def dfs(node, values):
            if node is None:
                return values
            
            if values and node.val >= max(values):
                values.append(node.val)
            if values == []:
                values.append(node.val)

            values = dfs(node.left, values)
            values = dfs(node.right, values)
            return values
        return len(dfs(root, values))