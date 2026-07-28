# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # I want to explicitly keep tracking of the good values instead of just sum it up.
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            values = []
            if node is None:
                return values

            if node.val >= maxVal:
                values.append(node.val)
            maxVal = max(node.val, maxVal)
            values += dfs(node.right, maxVal)
            values += dfs(node.left, maxVal)
            return values
        values = dfs(root, root.val)
        return len(values)
            