# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def aux(node, targetSum):
            if node is None:
                return False

            if node.left is None and node.right is None:
                if node.val == targetSum:
                    return True

            
            if aux(node.left, targetSum-node.val) is True:
                return True
            if aux(node.right, targetSum-node.val) is True:
                return True
            
            return False
        
        return aux(root, targetSum)
