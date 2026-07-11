# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, targetSum):
            if node is None:
                return False

            if node.left is None and node.right is None:
                if node.val == targetSum:
                    return True

            # this can be rewrite as:
            # return dfs(left) or dfs(right)
            if dfs(node.left, targetSum-node.val) is True:
                return True
            if dfs(node.right, targetSum-node.val) is True:
                return True
            
            return False
        
        return dfs(root, targetSum)
